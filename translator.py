import llvmlite.ir as ir 
import json

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



class TranslatorToLLVM(PrintFormatMixin):
    choose_type_entry = {
        "void": ir.VoidType(),
        "int": ir.IntType(32),
        'double': ir.DoubleType(),
        }
    def __init__(self):
        self.module = ir.Module("nevermoreCompile")
        self.ast = None
        self.print_func = None
        self.print_func_float = None
        self.builder = None
        self.format_str_loaded_int = None
        self.format_str_loaded_float = None
        self.variables = {}
        self.functions = {}
        self.main_func = None   
        
        
    def item_bypass(self, items:dict, builder = None):

        builder = builder if builder else self.builder
        for item in items:
            if 'stat' in item:
                stat = item['stat']
                if 'assignmentStatement' in stat:
                    self.assign_statement(stat, builder)
                elif 'printStatement' in stat:
                    self.print_statement(stat, builder)
            elif 'whileStatement' in item:
                self.while_statement(item,builder)
            elif 'doWhileStatement' in item:
                self.do_while_statement(item, builder)
            elif 'forStatement' in item:
                self.for_statement(item,builder)
            elif 'ifStatement' in item:
                self.if_statement(item, builder) 
            elif 'ifElseStatement' in item:
                self.if_else_statement(item, builder)   
            elif 'functionStatement' in item:
                if item['functionStatement']['name'] not in self.functions:
                    self.function_statement(item)
            elif 'functionCall' in item:
                self.function_call(item)
        
        
    def json_reader(self, input_file: str = "output_files/ast.json") -> None:
        with open(input_file, "r") as f:
            self.ast = json.load(f)
            
    def ll_writer(self, output_file: str = "output_files/output.ll") -> None:
        with open(output_file, "w") as f:
            f.write(str(self.module))
    
    
    
    def builder_init(self) -> None:
        try:
            global_stat = self.ast[1]
        except:
            global_stat = None
        if self.ast[0]['functionStatement']['name'] == "main":
            func_name = self.ast[0]['functionStatement']['name']
            func_type = self.choose_type_entry[self.ast[0]['functionStatement']["type"]]
            self.ast = self.ast[0]['functionStatement']['body']
        else:
            func_name = 'main'
            func_type = ir.VoidType()
            
        main_func_type = ir.FunctionType(func_type, [])
        main_func = ir.Function(self.module, main_func_type, name=func_name)
        self.main_func = main_func
        block = main_func.append_basic_block(name=f"entry.{func_name}")
        builder = ir.IRBuilder(block)
        self.builder = builder
        self.functions[func_name] = builder
        super().__init__(self.module)
        if global_stat:
            self.global_variable_statement(global_stat)

        
    
    def evaluate_expression(self, expr, builder = None):
        builder = builder if builder else self.builder
        if 'functionCall' in expr:
            expr = expr['functionCall']
            func_name = expr['name']
            params = expr['params']
            value = builder.call(self.functions[func_name]['func'], params)
            return value
        elif expr['type'] == 'INT' or expr['type'] == 'int':
            return ir.Constant(ir.IntType(32), expr['value'])
        elif expr['type'] == 'DOUBLE' or expr['type'] == 'double':
            return ir.Constant(ir.DoubleType(), expr['value'])
        elif expr['type'] == 'ID' or expr['type'] == 'VAR':
            try:
                return self.variables[expr['value']]['var']
            except:
                return self.variables[expr['value']]
        elif expr['type'] in ['DIV', 'MUL', 'ADD', 'SUB']:
            return self.execute_math_operation(expr, builder)
        else:
            raise ValueError(f"Unsupported expression type: {expr['type']}")

    def execute_math_operation(self, expr, builder = None):
        builder = builder if builder else self.builder
        left_value = self.evaluate_expression(expr['left'], builder)
        right_value = self.evaluate_expression(expr['right'], builder)
        
        if isinstance(left_value, ir.AllocaInstr) or isinstance(left_value, ir.GlobalVariable):
            left_value = builder.load(left_value)
        if isinstance(right_value, ir.AllocaInstr) or isinstance(right_value, ir.GlobalVariable):
            right_value = builder.load(right_value)
        
        if isinstance(left_value.type, ir.IntType) and isinstance(right_value.type, ir.IntType):
        
            if expr['type'] == 'DIV':
                return builder.udiv(left_value, right_value)
            elif expr['type'] == 'MUL':
                return builder.mul(left_value, right_value)
            elif expr['type'] == 'ADD':
                return builder.add(left_value, right_value)
            elif expr['type'] == 'SUB':
                return builder.sub(left_value, right_value)
            else:
                raise ValueError(f"Unsupported math operation: {expr['type']}")
        
        elif isinstance(left_value.type, ir.DoubleType) or isinstance(right_value.type, ir.DoubleType):
            if isinstance(left_value.type, ir.IntType):
                left_value = builder.sitofp(left_value, ir.DoubleType())
            
            elif isinstance(right_value.type, ir.IntType):
                right_value = builder.sitofp(right_value, ir.DoubleType())
                
            if expr['type'] == 'DIV':
                return builder.fdiv(left_value, right_value)
            elif expr['type'] == 'MUL':
                return builder.fmul(left_value, right_value)
            elif expr['type'] == 'ADD':
                return builder.fadd(left_value, right_value)
            elif expr['type'] == 'SUB':
                return builder.fsub(left_value, right_value)
            else:
                raise ValueError(f"Unsupported math operation: {expr['type']}")
    
        
        
    
    def assign_statement(self, stat:dict, builder = None):
        builder = builder if builder else self.builder
        assigment = stat['assignmentStatement']
        var_name = assigment['ID']
        expr = assigment['expr'][0]
        
        
        
        value = self.evaluate_expression(expr, builder)

        if var_name not in self.variables and assigment['type'] == 'int' or assigment['type'] == 'INT':
            var = builder.alloca(ir.IntType(32), name=var_name)
            self.variables[var_name] = {"var":var, "func": builder.function.name}
            
            
        elif var_name not in self.variables and assigment['type'] == 'double' or assigment['type'] == 'DOUBLE':
            var = builder.alloca(ir.DoubleType(), name=var_name)
            self.variables[var_name] = {"var":var, "func": builder.function.name}
            
        
        elif not isinstance(self.variables[var_name], ir.GlobalVariable): 
            
            if var_name in self.variables and self.variables[var_name]['func'] == builder.function.name and assigment['type'] == 'int' or assigment['type'] == 'INT':
                var = self.variables[var_name]['var']
                
            elif var_name in self.variables and self.variables[var_name]['func'] == builder.function.name and assigment['type'] == 'double' or assigment['type'] == 'DOUBLE':
                var = self.variables[var_name]['var']
                
            elif var_name in self.variables and self.variables[var_name]['func'] != builder.function.name and assigment['type'] == 'int' or assigment['type'] == 'INT':
                raise ValueError(f"{var_name} не сущетсвует в области")
                
            elif var_name in self.variables and self.variables[var_name]['func'] != builder.function.name and assigment['type'] == 'double' or assigment['type'] == 'DOUBLE':
                raise ValueError(f"{var_name} не сущетсвует в области")
                
        else:
            var = self.variables[var_name]
        
        
        
        if isinstance(value, ir.AllocaInstr) or isinstance(value, ir.GlobalVariable):
            builder.store(builder.load(value), var)
        else:
            builder.store(value, var)
        
        
        
        
    def print_expr(self, expr: dict, builder= None):
        builder = builder if builder else self.builder
        if expr['type'] == 'INT' or expr['type'] == 'int':
            return int(expr['value'])
        elif expr['type'] == 'DOUBLE' or expr['type'] == 'double':
            return float(expr['value'])
        elif expr['type'] == 'ID' or expr['type'] == 'VAR':
            if not isinstance(self.variables[expr['value']], ir.GlobalVariable):
                if expr['value'] in self.variables and builder.function.name != self.variables[expr['value']]['func']: 
                    raise ValueError(f"{expr['value']} не сущетсвует в области видимости {builder.function.name}, а существует только в {self.variables[expr['value']]['func']}")
                else:
                    try:
                        return self.variables[expr['value']]['var']
                    except:
                        return self.variables[expr['value']]
            else:
                try:
                    return self.variables[expr['value']]['var']
                except:
                    return self.variables[expr['value']]
        else:
            raise ValueError(f"Unsupported expression type: {expr['type']}")
    
    def choose_print_type(self, value, builder = None):
        builder = builder if builder else self.builder
        
        self.create_print_function(value, builder)
        

    
    def print_statement(self, stat:dict, builder = None):
        builder = builder if builder else self.builder
        print_statement = stat['printStatement']
        expr = print_statement['expr']
        
        value = self.print_expr(expr, builder)
        if isinstance(value, ir.AllocaInstr) or isinstance(value, ir.GlobalVariable):
            value = builder.load(value)
        
        self.choose_print_type(value, builder)
            
        
        
        
    def while_statement(self, stat: dict, builder = None):
        builder = builder if builder else self.builder
        while_statement = stat['whileStatement']
        condition = while_statement['condition']
        while_body = while_statement['body']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if  function_name != 'main' else self.main_func
        
        
        left_cond = self.evaluate_expression(condition['left'], builder)
        right_cond = self.evaluate_expression(condition['right'],builder)
        op = condition['op']
        
        while_block = func.append_basic_block(name="while")
        end_while_block = func.append_basic_block(name="end_while")
        while_cond = builder.icmp_unsigned(op, 
                                                builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                                 builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        builder.cbranch(while_cond, while_block, end_while_block)
        
        builder.position_at_end(while_block)
        
        self.item_bypass(while_body, builder)
        
        auto_inc = builder.add(builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                    ir.Constant(ir.IntType(32), 1))
        builder.store(auto_inc, left_cond)
        
        while_cond = builder.icmp_unsigned(op, 
                                                builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                                builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        
        builder.cbranch(while_cond, while_block, end_while_block)
        builder.position_at_end(end_while_block)
    
    def do_while_statement(self, stat: dict, builder = None):
        builder = builder if builder else self.builder
        do_while_statement = stat['doWhileStatement']
        condition = do_while_statement['condition']
        do_while_body = do_while_statement['body']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if  function_name != 'main' else self.main_function
    
        left_cond = self.evaluate_expression(condition['left'], builder)
        right_cond = self.evaluate_expression(condition['right'], builder)
        op = condition['op']
        do_while_start_block = func.append_basic_block(name="do_while_start")
        do_while_body_block = func.append_basic_block(name="do_while_body")
        do_while_end_block = func.append_basic_block(name="do_while_end")
        
        builder.branch(do_while_start_block)
        builder.position_at_end(do_while_start_block)
        
        self.item_bypass(do_while_body, builder)

        do_while_cond = builder.icmp_unsigned(op,
                                                builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                                builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        builder.cbranch(do_while_cond, do_while_body_block, do_while_end_block)
        builder.position_at_end(do_while_body_block)
        
        auto_inc = builder.add(builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                    ir.Constant(ir.IntType(32), 1))
        builder.store(auto_inc, left_cond)
        
        builder.branch(do_while_start_block)
        builder.position_at_end(do_while_end_block)                                    
    
    def for_statement(self, stat: dict, builder = None):
        builder = builder if builder else self.builder
        for_statement = stat['forStatement']
        for_init = for_statement['init']
        condition = for_statement['condition']
        for_modify = for_statement['modify']
        for_body = for_statement['body']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if  function_name != 'main' else self.main_function
        
        if 'stat' in for_init:
            stat = for_init['stat']
            if 'assignmentStatement' in stat:
                self.assign_statement(stat)
                
        left_cond = self.evaluate_expression(condition['left'], builder)
        right_cond = self.evaluate_expression(condition['right'], builder)
        op = condition['op']
        
        for_body_block = func.append_basic_block(name="for_body")
        exit_block = func.append_basic_block(name="exit_for")
        for_cond = builder.icmp_unsigned(op,
                                            builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                            builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        builder.cbranch(for_cond, for_body_block, exit_block)
        
        builder.position_at_end(for_body_block)
        self.item_bypass(for_body, builder)
                
        auto_inc = builder.add(builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                    ir.Constant(ir.IntType(32), 1))
        builder.store(auto_inc, left_cond)
        
        for_cond = builder.icmp_unsigned(op,
                                            builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                            builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        builder.cbranch(for_cond, for_body_block, exit_block)
        builder.position_at_end(exit_block)
        
        
        
    def if_statement(self, stat: dict, builder = None):
        builder = builder if builder else self.builder
        if_statement = stat['ifStatement']
        condition = if_statement['condition']
        if_body = if_statement['body']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if  function_name != 'main' else self.main_func
        
        left_cond = self.evaluate_expression(condition['left'], builder)
        right_cond = self.evaluate_expression(condition['right'], builder)
        op = condition['op']
        
        if_cond = builder.icmp_signed(op,
                                        builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                        builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        then_block = func.append_basic_block(name="if.then")
        end_block = func.append_basic_block(name="if.end")
        
        builder.cbranch(if_cond, then_block, end_block)
        
        builder.position_at_start(then_block)
        
        self.item_bypass(if_body, builder)
        
        builder.branch(end_block)
        builder.position_at_start(end_block)
                
    def if_else_statement(self, stat: dict, builder = None):
        builder = builder if builder else self.builder
        if_else_statement = stat['ifElseStatement']
        condition = if_else_statement['condition']
        if_body = if_else_statement['ifBody']
        if_else_body = if_else_statement['elseBody']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if function_name != 'main' else self.main_func
        
        left_cond = self.evaluate_expression(condition['left'], builder)
        right_cond = self.evaluate_expression(condition['right'], builder)
        op = condition['op']
        
        if_cond = builder.icmp_signed(op,
                                        builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                        builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond)
        
        then_block = func.append_basic_block(name="if.then")
        else_block = func.append_basic_block(name="if.else")
        end_block = func.append_basic_block(name="if.end")
        
        
        builder.cbranch(if_cond, then_block, else_block)
        
        builder.position_at_start(then_block)
        self.item_bypass(if_body, builder)
    
        builder.branch(end_block)
        
        builder.position_at_start(else_block)
        
        self.item_bypass(if_else_body, builder)
                
        builder.branch(end_block)
        
        builder.position_at_start(end_block)
        
        
    
    def global_variable_statement(self, stat: dict):
        g_vars_statement = stat['globalStatement']
        for item, value in g_vars_statement.items():
            if value == 'int':
                int_type = ir.IntType(32)
                global_var = ir.GlobalVariable(self.module, int_type, item)
                global_var.initializer = ir.Constant(int_type, 0)
                self.variables[item] = global_var
                
    def function_statement(self, statement):
        func_statement = statement["functionStatement"]
        func_name  = func_statement['name']
        func_body = func_statement['body']
        f_type = func_statement["type"]
        args = func_statement['args']
        type_entry = self.choose_type_entry[f_type]
        return_ = func_statement['return']
        
        func_type = ir.FunctionType(type_entry, [self.choose_type_entry[arg] for key, arg in args.items()])
        func = ir.Function(self.module, func_type, name=func_name)
        block = func.append_basic_block(name='entry')
        builder = ir.IRBuilder(block)
        self.functions[func_name] = {"builder": builder, "func": func}
        
        self.item_bypass(func_body, builder)
        type_ret = self.check_data_type(return_) if f_type != 'void' else None
        if f_type == 'void':
            self.functions[func_name]['builder'].ret_void()
        elif type_ret == 'str':
            self.functions[func_name]['builder'].ret(builder.load(self.variables[return_]['var']))
        elif type_ret == 'int':
            self.functions[func_name]['builder'].ret(ir.Constant(ir.IntType(32), int(return_)))
        elif type_ret == 'double':
            self.functions[func_name]['builder'].ret(ir.Constant(ir.Double(), float(return_)))
        
    def check_data_type(self, s):
        try:
            int(s)
            return "int"
        except ValueError:
            try:
                float(s)
                return "double"
            except ValueError:
                return "str"    
        
    def function_call(self, stat: dict):
        function_name = stat['functionCall']['name']
        function_type = stat['functionCall']['type']
        
        func = self.functions[function_name]
        if function_type == 'void':
            self.builder.call(func['func'], [])
        
        
    
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
            elif 'functionStatement' in item:
                if item['functionStatement']['name'] not in self.functions:
                    self.function_statement(item)
            elif 'functionCall' in item:
                self.function_call(item)
            
        self.builder.ret_void()


if __name__ == '__main__':
    tolvm = TranslatorToLLVM()
    tolvm.json_reader()
    tolvm.builder_init()
    tolvm.ast_bypass()
    tolvm.ll_writer()
    print("Промежуточный код готов!")


