import json
import llvmlite.ir as ir
import tempfile


class PrintFormatMixin:
    def __init__(self, module) -> None:
        self.int32_type = ir.IntType(32)
        self.double_type = ir.DoubleType()
        self.int8_ptr_type = ir.IntType(8).as_pointer()
        printf_type = ir.FunctionType(ir.IntType(32), [self.int8_ptr_type], var_arg=True)
        self.printf_func = ir.Function(module, printf_type, "printf")

    def create_print_function(self, value, builder):
        if isinstance(value, int):
            format_str = "%d\n\0"
            value_type = self.int32_type
            value_ptr = ir.Constant(ir.IntType(32), value)
        elif isinstance(value, float):
            format_str = "%f\n\0"
            value_type = self.double_type
            value_ptr = ir.Constant(ir.DoubleType(), value)
        else:
            if value.type == ir.IntType(32):
                format_str = "%d\n\0"
            elif value.type == ir.DoubleType():
                format_str = "%f\n\0"
            else:
                raise ValueError("Unsupported value type")
            value_ptr = value

        format_str_array = ir.ArrayType(ir.IntType(8), len(format_str))
        format_str_ptr = builder.alloca(format_str_array)
        format_str_const = ir.Constant(format_str_array, bytearray(format_str.encode("utf-8")))
        builder.store(format_str_const, format_str_ptr)

        builder.call(self.printf_func, [builder.bitcast(format_str_ptr, self.int8_ptr_type), value_ptr])


class ReadWriteMixin:

    def input_code_reader(self, input_file: str) -> str:
        if isinstance(input_file, tempfile._TemporaryFileWrapper):
            input_file = input_file.name

        with open(input_file, 'r') as file:
            return file.read()

    def ast_writer(self, output_file) -> None:
        with open(output_file, 'w') as file:
            file.write(json.dumps(self.ast, indent=1))

    def ast_reader(self, input_file: str) -> None:
        with open(input_file, "r") as f:
            self.ast = json.load(f)

    def ll_writer(self, output_file) -> None:
        with open(output_file, "w") as f:
            f.write(str(self.module))

    def ll_reader(self) -> None:
        with open(self.ll_file, 'r') as f:
            self.ll_file = f.read()


class LibFuncMixin:
    def pow_func(self):
        int_pow_func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)]) 
        int_pow_func = ir.Function(self.module, int_pow_func_type, name="int_pow")
        entry_builder = ir.IRBuilder(int_pow_func.append_basic_block(name="entry"))
        result = entry_builder.alloca(ir.IntType(32), name="result")
        entry_builder.store(ir.Constant(ir.IntType(32), 1), result)

        loop_block = int_pow_func.append_basic_block(name="loop")
        exit_block = int_pow_func.append_basic_block(name="exit")
        
        base = int_pow_func.args[0]
        exponent_ptr = entry_builder.alloca(ir.IntType(32), name="exponent_ptr")
        entry_builder.store(int_pow_func.args[1], exponent_ptr)

        entry_builder.branch(loop_block)
        loop_builder = ir.IRBuilder(loop_block)

        current_result = loop_builder.load(result, name="current_result")
        current_base = base

        mul = loop_builder.mul(current_result, current_base, name="mul")
        loop_builder.store(mul, result)

        current_exponent = loop_builder.load(exponent_ptr, name="current_exponent")
        decremented_exponent = loop_builder.sub(current_exponent, ir.Constant(ir.IntType(32), 1), name="decremented_exponent")
        loop_builder.store(decremented_exponent, exponent_ptr)

        cmp = loop_builder.icmp_signed(">", decremented_exponent, ir.Constant(ir.IntType(32), 0))
        loop_builder.cbranch(cmp, loop_block, exit_block)
        
        exit_builder = ir.IRBuilder(exit_block)
        final_result = exit_builder.load(result)
        
        exit_builder.ret(final_result)

        self.functions["int_pow"] = int_pow_func
    
    def abs_func(self):
        abs_func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32)]) 
        abs_func = ir.Function(self.module, abs_func_type, name="abs")
        entry_block = abs_func.append_basic_block(name="entry")
        entry_builder = ir.IRBuilder(entry_block)
        
        arg_val = abs_func.args[0]
        
        result = entry_builder.sub(
            ir.Constant(ir.IntType(32), 0),
            arg_val,
            name="result"
        )

        cmp = entry_builder.icmp_signed("<", arg_val, ir.Constant(ir.IntType(32), 0))
        result = entry_builder.select(cmp, result, arg_val)
        
        entry_builder.ret(result)
        
        self.functions["abs"] = {"builder": self.builder, "func": abs_func}

    def abs_func_float(self):
        abs_func_type = ir.FunctionType(ir.DoubleType(), [ir.DoubleType()])
        abs_func = ir.Function(self.module, abs_func_type, name="absf")
        entry_block = abs_func.append_basic_block(name="entry")
        entry_builder = ir.IRBuilder(entry_block)
        
        arg_val = abs_func.args[0]
        
        result = entry_builder.fsub(
            ir.Constant(ir.DoubleType(), 0.0),
            arg_val,
            name="result"
        )

        cmp = entry_builder.fcmp_unordered("<", arg_val, ir.Constant(ir.DoubleType(), 0.0))
        result = entry_builder.select(cmp, result, arg_val)
        
        entry_builder.ret(result)
        
        self.functions["absf"] = {"builder": entry_builder, "func": abs_func}