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
