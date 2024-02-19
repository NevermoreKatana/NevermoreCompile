import llvmlite.ir as ir 
import json

class PrintFormatMixin:
    def __init__(self) -> None:
        self.g_const_print_int_format()

    def g_const_print_int_format(self):
        printf_func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()], var_arg=True)
        printf_func = ir.Function(self.module, printf_func_type, name="printf")

        format_str_int = "%d\n"
        format_str_ptr_int = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(format_str_int)),
                                       name="format_str")
        format_str_ptr_int.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(format_str_int)),
                                             bytearray(format_str_int.encode()))

        format_str_loaded_int = self.builder.gep(format_str_ptr_int, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)])
        format_str_loaded_int = self.builder.bitcast(format_str_ptr_int, ir.IntType(8).as_pointer())

        self.format_str_loaded_int = format_str_loaded_int
        self.print_func = printf_func
        return



class TranslatorToLLVM(PrintFormatMixin):
    def __init__(self):
        self.module = ir.Module("nevermoreCompile")
        self.ast = None
        self.print_func = None
        self.builder = None
        self.format_str_loaded_int = None
        self.format_str_loaded_str = None
        self.variables = {}
        self.functions = {}
        self.main_func = None   
        
    def item_bypass(self, items:dict):
        for item in items:
            if 'stat' in item:
                stat = item['stat']
                if 'assignmentStatement' in stat:
                    self.assign_statement(stat)
                elif 'printStatement' in stat:
                    self.print_statement(stat)
            elif 'whileStatement' in item:
                self.while_statement(item)
            elif 'doWhileStatement' in item:
                self.do_while_statement(item)
            elif 'forStatement' in item:
                self.for_statement(item)
            elif 'ifStatement' in item:
                self.if_statement(item) 
            elif 'ifElseStatement' in item:
                self.if_else_statement(item)   
        
        
    def json_reader(self, input_file: str = "output_files/ast.json") -> None:
        with open(input_file, "r") as f:
            self.ast = json.load(f)
            
    def ll_writer(self, output_file: str = "output_files/output.ll") -> None:
        with open(output_file, "w") as f:
            f.write(str(self.module))
            
    def builder_init(self) -> None:
        main_func_type = ir.FunctionType(ir.VoidType(), [])
        main_func = ir.Function(self.module, main_func_type, name="main")
        self.main_func = main_func
        block = main_func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        self.builder = builder

        super().__init__()
    
    def evaluate_expression(self, expr):

        if expr['type'] == 'INT' or expr['type'] == 'int':
            return ir.Constant(ir.IntType(32), expr['value'])
        elif expr['type'] == 'ID' or expr['type'] == 'VAR':
            return self.variables[expr['value']]
        elif expr['type'] in ['DIV', 'MUL', 'ADD', 'SUB']:
            return self.execute_math_operation(expr)
        else:
            raise ValueError(f"Unsupported expression type: {expr['type']}")

    def execute_math_operation(self, expr):
        left_value = self.evaluate_expression(expr['left'])
        right_value = self.evaluate_expression(expr['right'])
        if isinstance(left_value, ir.AllocaInstr) or isinstance(left_value, ir.GlobalVariable):
            left_value = self.builder.load(left_value)
        if isinstance(right_value, ir.AllocaInstr) or isinstance(right_value, ir.GlobalVariable):
            right_value = self.builder.load(right_value)
        if expr['type'] == 'DIV':
            return self.builder.udiv(left_value, right_value)
        elif expr['type'] == 'MUL':
            return self.builder.mul(left_value, right_value)
        elif expr['type'] == 'ADD':
            return self.builder.add(left_value, right_value)
        elif expr['type'] == 'SUB':
            return self.builder.sub(left_value, right_value)
        else:
            raise ValueError(f"Unsupported math operation: {expr['type']}")
        
    
        
        
    
    def assign_statement(self, stat:dict):
        assigment = stat['assignmentStatement']
        var_name = assigment['ID']
        expr = assigment['expr'][0]

        
        
        value = self.evaluate_expression(expr)

        
        if var_name not in self.variables:
            var = self.builder.alloca(ir.IntType(32), name=var_name)
            self.variables[var_name] = var
        else:
            var = self.variables[var_name]
        
        if isinstance(value, ir.AllocaInstr) or isinstance(value, ir.GlobalVariable):
            self.builder.store(self.builder.load(value), var)
        else:
            self.builder.store(value, var)
        
        
        
    def print_expr(self, expr: dict):
        if expr['type'] == 'INT' or expr['type'] == 'int':
            return int(expr['value'])
        elif expr['type'] == 'ID' or expr['type'] == 'VAR':
            return self.variables[expr['value']]
        else:
            raise ValueError(f"Unsupported expression type: {expr['type']}")
    
    def choose_print_type(self, value, builder = None):
        builder = builder if builder else self.builder
        builder.call(self.print_func, [self.format_str_loaded_int, ir.Constant(ir.IntType(32), value)])

    
    def print_statement(self, stat:dict):
        print_statement = stat['printStatement']
        expr = print_statement['expr']
        print(expr)
        
        value = self.print_expr(expr)
        if isinstance(value, ir.AllocaInstr) or isinstance(value, ir.GlobalVariable):
            value = f'%"{self.builder.load(value).name}"'
        
        self.choose_print_type(value, self.builder)
        
    def while_statement(self, stat: dict):
        while_statement = stat['whileStatement']
        condition = while_statement['condition']
        while_body = while_statement['body']
        
        left_cond = self.evaluate_expression(condition['left'])
        right_cond = self.evaluate_expression(condition['right'])
        op = condition['op']
        
        while_block = self.main_func.append_basic_block(name="while")
        end_while_block = self.main_func.append_basic_block(name="end_while")
        
        while_cond = self.builder.icmp_unsigned(op, 
                                                self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                                 self.builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        self.builder.cbranch(while_cond, while_block, end_while_block)
        
        self.builder.position_at_end(while_block)
        self.item_bypass(while_body)
        
        auto_inc = self.builder.add(self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                    ir.Constant(ir.IntType(32), 1))
        self.builder.store(auto_inc, left_cond)
        
        while_cond = self.builder.icmp_unsigned(op, 
                                                self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                                 self.builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        
        self.builder.cbranch(while_cond, while_block, end_while_block)
        self.builder.position_at_end(end_while_block)
    
    def do_while_statement(self, stat: dict):
        do_while_statement = stat['doWhileStatement']
        condition = do_while_statement['condition']
        do_while_body = do_while_statement['body']
    
        left_cond = self.evaluate_expression(condition['left'])
        right_cond = self.evaluate_expression(condition['right'])
        op = condition['op']
        
        do_while_start_block = self.main_func.append_basic_block(name="do_while_start")
        do_while_body_block = self.main_func.append_basic_block(name="do_while_body")
        do_while_end_block = self.main_func.append_basic_block(name="do_while_end")
        
        self.builder.branch(do_while_start_block)
        self.builder.position_at_end(do_while_start_block)
        
        self.item_bypass(do_while_body)

        do_while_cond = self.builder.icmp_unsigned(op,
                                                   self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                                 self.builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        self.builder.cbranch(do_while_cond, do_while_body_block, do_while_end_block)
        self.builder.position_at_end(do_while_body_block)
        
        auto_inc = self.builder.add(self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                    ir.Constant(ir.IntType(32), 1))
        self.builder.store(auto_inc, left_cond)
        
        self.builder.branch(do_while_start_block)
        self.builder.position_at_end(do_while_end_block)                                    
    
    def for_statement(self, stat: dict):
        for_statement = stat['forStatement']
        for_init = for_statement['init']
        condition = for_statement['condition']
        for_modify = for_statement['modify']
        for_body = for_statement['body']
        
        if 'stat' in for_init:
            stat = for_init['stat']
            if 'assignmentStatement' in stat:
                self.assign_statement(stat)
                
        left_cond = self.evaluate_expression(condition['left'])
        right_cond = self.evaluate_expression(condition['right'])
        op = condition['op']
        
        for_body_block = self.main_func.append_basic_block(name="for_body")
        exit_block = self.main_func.append_basic_block(name="exit_for")
        for_cond = self.builder.icmp_unsigned(op,
                                                self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                                self.builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        self.builder.cbranch(for_cond, for_body_block, exit_block)
        
        self.builder.position_at_end(for_body_block)
        self.item_bypass(for_body)
                
        auto_inc = self.builder.add(self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                    ir.Constant(ir.IntType(32), 1))
        self.builder.store(auto_inc, left_cond)
        
        for_cond = self.builder.icmp_unsigned(op,
                                                self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                                self.builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        self.builder.cbranch(for_cond, for_body_block, exit_block)
        self.builder.position_at_end(exit_block)
        
        
        
    def if_statement(self, stat: dict):
        if_statement = stat['ifStatement']
        condition = if_statement['condition']
        if_body = if_statement['body']
        
        left_cond = self.evaluate_expression(condition['left'])
        right_cond = self.evaluate_expression(condition['right'])
        op = condition['op']
        
        if_cond = self.builder.icmp_signed(op,
                                            self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                            self.builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        then_block = self.main_func.append_basic_block(name="if.then")
        end_block = self.main_func.append_basic_block(name="if.end")
        
        self.builder.cbranch(if_cond, then_block, end_block)
        
        self.builder.position_at_start(then_block)
        
        self.item_bypass(if_body)
        
        self.builder.branch(end_block)
        self.builder.position_at_start(end_block)
                
    def if_else_statement(self, stat: dict):
        if_else_statement = stat['ifElseStatement']
        condition = if_else_statement['condition']
        if_else_body = if_else_statement['elseBody']
        
        left_cond = self.evaluate_expression(condition['left'])
        right_cond = self.evaluate_expression(condition['right'])
        op = condition['op']
        
        if_cond = self.builder.icmp_signed(op,
                                            self.builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                            self.builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        then_block = self.main_func.append_basic_block(name="if.then")
        else_block = self.main_func.append_basic_block(name="if.else")
        end_block = self.main_func.append_basic_block(name="if.end")
        
        
        self.builder.cbranch(if_cond, then_block, else_block)
        
        self.builder.position_at_start(then_block)
        self.item_bypass(if_else_body)
    
        self.builder.branch(end_block)
        
        self.builder.position_at_start(else_block)
        
        for item in if_else_body:
            if 'stat' in item:
                stat = item['stat']
                if 'assignmentStatement' in stat:
                    self.assign_statement(stat)
                elif 'printStatement' in stat:
                    self.print_statement(stat)
            elif 'whileStatement' in item:
                self.while_statement(item)
            elif 'doWhileStatement' in item:
                self.do_while_statement(item)
            elif 'forStatement' in item:
                self.for_statement(item)
                
        self.builder.branch(end_block)
        
        self.builder.position_at_start(end_block)
        
        
    
    def global_variable_statement(self, stat: dict):
        g_vars_statement = stat['globalStatement']
        for item, value in g_vars_statement.items():
            if value == 'int':
                int_type = ir.IntType(32)
                global_var = ir.GlobalVariable(self.module, int_type, item)
                global_var.initializer = ir.Constant(int_type, 0)
                self.variables[item] = global_var
    
    
    def ast_bypass(self) -> None:
        for item in self.ast:
            if 'stat' in item:
                stat = item['stat']
                if 'assignmentStatement' in stat:
                    self.assign_statement(stat)
                elif 'printStatement' in stat:
                    self.print_statement(stat)
            elif 'whileStatement' in item:
                self.while_statement(item)
            elif 'doWhileStatement' in item:
                self.do_while_statement(item)
            elif 'forStatement' in item:
                self.for_statement(item)
            elif 'ifStatement' in item:
                self.if_statement(item) 
            elif 'ifElseStatement' in item:
                self.if_else_statement(item)   
            elif 'globalStatement' in item:
                self.global_variable_statement(item)
            
        self.builder.ret_void()


if __name__ == '__main__':
    tolvm = TranslatorToLLVM()
    tolvm.json_reader()
    tolvm.builder_init()
    tolvm.ast_bypass()
    tolvm.ll_writer()
    print("Промежуточный код готов!")






