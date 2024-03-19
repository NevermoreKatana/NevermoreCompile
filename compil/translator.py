import llvmlite.ir as ir
import json
from ini import *
import sys
from mixins import PrintFormatMixin, CheckersMixin


class TranslatorToLLVM(PrintFormatMixin, CheckersMixin):
    choose_type_entry = {
        "void": ir.VoidType(),
        "int": ir.IntType(32),
        'double': ir.DoubleType(),
    }

    def __init__(self):
        self.module = ir.Module("nevermoreCompile")
        self.module.triple = 'x86_64-pc-linux-gnu'
        self.ast = None
        self.print_func = None
        self.print_func_float = None
        self.builder = None
        self.format_str_loaded_int = None
        self.format_str_loaded_float = None
        self.variables = {}
        self.functions = {}
        self.main_func = None

    def item_bypass(self, items: dict, builder=None):

        builder = builder if builder else self.builder
        for item in items:
            if 'stat' in item:
                stat = item['stat']
                if 'assignmentStatement' in stat:
                    self.assign_statement(stat, builder)
                elif 'printStatement' in stat:
                    self.print_statement(stat, builder)
            elif 'whileStatement' in item:
                self.while_statement(item, builder)
            elif 'doWhileStatement' in item:
                self.do_while_statement(item, builder)
            elif 'forStatement' in item:
                self.for_statement(item, builder)
            elif 'ifStatement' in item:
                self.if_statement(item, builder)
            elif 'ifElseStatement' in item:
                self.if_else_statement(item, builder)
            elif 'functionStatement' in item:
                if item['functionStatement']['name'] not in self.functions:
                    self.function_statement(item)
            elif 'functionCall' in item:
                self.function_call(item, builder)
            elif 'return' in item:
                self.return_statement(item, builder)

    def json_reader(self, input_file: str = ast_output_file) -> None:
        with open(input_file, "r") as f:
            self.ast = json.load(f)

    def ll_writer(self, output_file: str = ll_output_file) -> None:
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

    def evaluate_expression(self, expr, builder=None):
        builder = builder if builder else self.builder
        if 'functionCall' in expr:
            expr = expr['functionCall']
            func_name = expr['name']
            function_args = expr['params']
            func = self.functions[func_name]
            expected_types = [arg.type for arg in func['func'].args]

            params = []
            for i, arg in enumerate(function_args):
                if arg in self.variables:
                    var_info = self.variables[arg]
                    arg_type = var_info['var'].type.pointee
                    if arg_type == expected_types[i]:
                        params.append(builder.load(var_info['var']))
                    else:
                        raise TypeError(f"Аргумент {i} должен быть типом '{expected_types[i]}', а не '{arg_type}'")

                elif isinstance(expected_types[i], ir.IntType):
                    try:
                        arg = int(arg)
                    except ValueError:
                        raise TypeError(f"Аргумент {i} должен быть типа 'int', а не 'double'")

                    params.append(ir.Constant(ir.IntType(32), arg))

                elif isinstance(expected_types[i], ir.DoubleType):
                    try:
                        arg = float(arg)
                        if arg.is_integer():
                            raise TypeError(f"Аргумент {i} должен быть типа 'double', а не 'int'")
                    except ValueError:
                        raise TypeError(f"Аргумент {i} должен быть типа 'double'")
                    params.append(ir.Constant(ir.DoubleType(), arg))
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
                try:
                    return self.variables[expr['value']]
                except:
                    return None
        elif expr['type'] in ['DIV', 'MUL', 'ADD', 'SUB']:
            return self.execute_math_operation(expr, builder)
        else:
            try:
                raise ValueError(f"Unsupported expression type: {expr['type']}")
            except ValueError as e:
                # print(str(e))
                sys.exit(1)

    def execute_math_operation(self, expr, builder=None):
        builder = builder if builder else self.builder
        func = builder.function
        cond_l = expr['left']
        cond_r = expr['right']

        left_value = self.evaluate_expression(cond_l, builder)
        right_value = self.evaluate_expression(cond_r, builder)

        if left_value is None:
            left_value = {'type': "VAR", 'value': cond_l['value'] + '_tmp'}
            left_value = self.evaluate_expression(left_value, builder)
        elif not isinstance(left_value, ir.GlobalVariable) and cond_l['type'] == 'VAR' and left_value.function != func:
            left_value = {'type': "VAR", 'value': cond_l['value'] + '_tmp'}
            left_value = self.evaluate_expression(left_value, builder)

        if right_value is None:
            right_value = {'type': "VAR", 'value': cond_r['value'] + '_tmp'}
            right_value = self.evaluate_expression(right_value, builder)
        elif not isinstance(right_value, ir.GlobalValue) and cond_r['type'] == 'VAR' and right_value.function != func:
            right_value = {'type': "VAR", 'value': cond_r['value'] + '_tmp'}
            right_value = self.evaluate_expression(right_value, builder)

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

    def assign_statement(self, stat: dict, builder=None):
        builder = builder if builder else self.builder
        assigment = stat['assignmentStatement']
        var_name = assigment['ID']
        expr = assigment['expr'][0]
        var_type = assigment['type']

        value = self.evaluate_expression(expr, builder)

        if var_name not in self.variables and var_type == 'int' or var_type == 'INT':
            var = builder.alloca(ir.IntType(32), name=var_name)
            self.variables[var_name] = {"var": var, "func": builder.function.name}


        elif var_name not in self.variables and var_type == 'double' or var_type == 'DOUBLE':
            var = builder.alloca(ir.DoubleType(), name=var_name)
            self.variables[var_name] = {"var": var, "func": builder.function.name}


        elif not isinstance(self.variables[var_name], ir.GlobalVariable):

            if var_name in self.variables and self.variables[var_name][
                'func'] == builder.function.name and var_type == 'int' or var_type == 'INT':
                var = self.variables[var_name]['var']

            elif var_name in self.variables and self.variables[var_name][
                'func'] == builder.function.name and var_type == 'double' or var_type == 'DOUBLE':
                var = self.variables[var_name]['var']

            elif var_name in self.variables and self.variables[var_name][
                'func'] != builder.function.name and var_type == 'int' or var_type == 'INT':
                var = builder.alloca(ir.IntType(32), name=var_name)
                self.variables[var_name] = {"var": var, "func": builder.function.name}

            elif var_name in self.variables and self.variables[var_name][
                'func'] != builder.function.name and var_type == 'double' or var_type == 'DOUBLE':
                var = builder.alloca(ir.DoubleType(), name=var_name)
                self.variables[var_name] = {"var": var, "func": builder.function.name}
        else:
            var = self.variables[var_name]
        if not isinstance(value.type, type(var.type.pointee)):
            try:
                raise TypeError(
                    f"Нельзя присвоить тип данных {value.type} переменной {var_name} с типом данных {var.type.pointee}")
            except TypeError as e:
                print(str(e))
                sys.exit(1)

        if isinstance(value, ir.AllocaInstr) or isinstance(value, ir.GlobalVariable):
            builder.store(builder.load(value), var)
        else:

            builder.store(value, var)

    def print_expr(self, expr: dict, builder=None):
        builder = builder if builder else self.builder
        if expr['type'] == 'INT' or expr['type'] == 'int':
            return int(expr['value'])
        elif expr['type'] == 'DOUBLE' or expr['type'] == 'double':
            return float(expr['value'])
        elif expr['type'] == 'ID' or expr['type'] == 'VAR':
            if not isinstance(self.variables[expr['value']], ir.GlobalVariable):
                if f"{expr['value']}_tmp" in self.variables:
                    return self.variables[f"{expr['value']}_tmp"]['var']
                if expr['value'] in self.variables and builder.function.name != self.variables[expr['value']]['func']:
                    try:
                        raise ValueError(
                            f"{expr['value']} не сущетсвует в области видимости {builder.function.name}, а существует только в {self.variables[expr['value']]['func']}")
                    except ValueError as e:
                        # print(str(e))
                        sys.exit(1)

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
            try:
                raise ValueError(f"Unsupported expression type: {expr['type']}")
            except ValueError as e:
                print(str(e))
                sys.exit(1)

    def choose_print_type(self, value, builder=None):
        builder = builder if builder else self.builder

        self.create_print_function(value, builder)

    def print_statement(self, stat: dict, builder=None):
        builder = builder if builder else self.builder
        print_statement = stat['printStatement']
        expr = print_statement['expr']

        value = self.print_expr(expr, builder)
        if isinstance(value, ir.AllocaInstr) or isinstance(value, ir.GlobalVariable):
            value = builder.load(value)

        self.choose_print_type(value, builder)

    def while_statement(self, stat: dict, builder=None):
        builder = builder if builder else self.builder
        while_statement = stat['whileStatement']
        condition = while_statement['condition']
        while_body = while_statement['body']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if function_name != 'main' else self.main_func
        op = condition['op']

        cond_l = condition['left']
        cond_r = condition['right']

        left_cond_ptr = self.evaluate_expression(cond_l, builder)
        right_cond_ptr = self.evaluate_expression(cond_r, builder)

        if cond_l['type'] == 'VAR' and left_cond_ptr.function != func:
            left_cond_ptr = {'type': "VAR", 'value': cond_l['value'] + '_tmp'}
            left_cond_ptr = self.evaluate_expression(left_cond_ptr, builder)

        if cond_r['type'] == 'VAR' and right_cond_ptr.function != func:
            right_cond_ptr = {'type': "VAR", 'value': cond_r['value'] + '_tmp'}
            right_cond_ptr = self.evaluate_expression(right_cond_ptr, builder)

        left_cond = builder.load(left_cond_ptr) if isinstance(left_cond_ptr, ir.AllocaInstr) else left_cond_ptr
        right_cond = builder.load(right_cond_ptr) if isinstance(right_cond_ptr, ir.AllocaInstr) else right_cond_ptr

        left_cond = builder.load(left_cond) if isinstance(left_cond.type, ir.PointerType) else left_cond
        right_cond = builder.load(right_cond) if isinstance(right_cond.type, ir.PointerType) else right_cond
        if isinstance(left_cond.type, ir.DoubleType) or isinstance(right_cond.type, ir.DoubleType):
            try:
                raise TypeError(f"Нельзя использовать значения типа double в условии цикла while")
            except TypeError as e:
                print(str(e))
                sys.exit(1)

        original_value = builder.load(left_cond_ptr)

        while_block = func.append_basic_block(name="while")
        end_while_block = func.append_basic_block(name="end_while")
        while_cond = builder.icmp_unsigned(op,
                                           left_cond,
                                           right_cond)

        builder.cbranch(while_cond, while_block, end_while_block)

        builder.position_at_end(while_block)

        self.item_bypass(while_body, builder)

        auto_inc = builder.add(builder.load(left_cond_ptr), ir.Constant(ir.IntType(32), 1))
        builder.store(auto_inc, left_cond_ptr)

        while_cond = builder.icmp_unsigned(op, builder.load(left_cond_ptr), right_cond)

        builder.cbranch(while_cond, while_block, end_while_block)
        builder.position_at_end(end_while_block)
        builder.store(original_value, left_cond_ptr)

    def do_while_statement(self, stat: dict, builder=None):
        builder = builder if builder else self.builder
        do_while_statement = stat['doWhileStatement']
        condition = do_while_statement['condition']
        do_while_body = do_while_statement['body']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if function_name != 'main' else self.main_func

        cond_l = condition['left']
        cond_r = condition['right']

        left_cond_ptr = self.evaluate_expression(cond_l, builder)
        right_cond_ptr = self.evaluate_expression(cond_r, builder)

        if cond_l['type'] == 'VAR' and left_cond_ptr.function != func:
            left_cond_ptr = {'type': "VAR", 'value': cond_l['value'] + '_tmp'}
            left_cond_ptr = self.evaluate_expression(left_cond_ptr, builder)

        if cond_r['type'] == 'VAR' and right_cond_ptr.function != func:
            right_cond_ptr = {'type': "VAR", 'value': cond_r['value'] + '_tmp'}
            right_cond_ptr = self.evaluate_expression(right_cond_ptr, builder)

        left_cond = builder.load(left_cond_ptr) if isinstance(left_cond_ptr, ir.AllocaInstr) else left_cond_ptr
        right_cond = builder.load(right_cond_ptr) if isinstance(right_cond_ptr, ir.AllocaInstr) else right_cond_ptr

        left_cond = builder.load(left_cond) if isinstance(left_cond.type, ir.PointerType) else left_cond
        right_cond = builder.load(right_cond) if isinstance(right_cond.type, ir.PointerType) else right_cond
        if isinstance(left_cond.type, ir.DoubleType) or isinstance(right_cond.type, ir.DoubleType):
            try:
                raise TypeError(f"Нельзя использовать значения типа double в условии цикла doWhile")
            except TypeError as e:
                print(str(e))
                sys.exit(1)
        op = condition['op']

        original_value = builder.load(left_cond_ptr)

        do_while_start_block = func.append_basic_block(name="do_while_start")
        do_while_body_block = func.append_basic_block(name="do_while_body")
        do_while_end_block = func.append_basic_block(name="do_while_end")

        builder.branch(do_while_start_block)
        builder.position_at_end(do_while_start_block)

        self.item_bypass(do_while_body, builder)

        do_while_cond = builder.icmp_unsigned(op,
                                              builder.load(left_cond_ptr), right_cond)
        builder.cbranch(do_while_cond, do_while_body_block, do_while_end_block)
        builder.position_at_end(do_while_body_block)

        auto_inc = builder.add(builder.load(left_cond_ptr),
                               ir.Constant(ir.IntType(32), 1))
        builder.store(auto_inc, left_cond_ptr)

        builder.branch(do_while_start_block)
        builder.position_at_end(do_while_end_block)
        builder.store(original_value, left_cond_ptr)

    def for_statement(self, stat: dict, builder=None):
        builder = builder if builder else self.builder
        for_statement = stat['forStatement']
        for_init = for_statement['init']
        condition = for_statement['condition']
        for_modify = for_statement['modify']['op']
        for_body = for_statement['body']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if function_name != 'main' else self.main_func

        if 'stat' in for_init:
            stat = for_init['stat']
            if 'assignmentStatement' in stat:
                self.assign_statement(stat, builder)

        left_cond = self.evaluate_expression(condition['left'], builder)
        right_cond = self.evaluate_expression(condition['right'], builder)
        op = condition['op']

        for_body_block = func.append_basic_block(name="for_body")
        exit_block = func.append_basic_block(name="exit_for")
        for_cond = builder.icmp_unsigned(op,
                                         builder.load(left_cond) if isinstance(left_cond,
                                                                               ir.AllocaInstr) else left_cond,
                                         builder.load(right_cond) if isinstance(right_cond,
                                                                                ir.AllocaInstr) else right_cond)

        builder.cbranch(for_cond, for_body_block, exit_block)

        builder.position_at_end(for_body_block)
        self.item_bypass(for_body, builder)
        if for_modify == '++':
            auto_inc = builder.add(builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                   ir.Constant(ir.IntType(32), 1))
        elif for_modify == '--':
            auto_inc = builder.sub(builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond,
                                   ir.Constant(ir.IntType(32), 1))
        builder.store(auto_inc, left_cond)

        for_cond = builder.icmp_unsigned(op,
                                         builder.load(left_cond) if isinstance(left_cond,
                                                                               ir.AllocaInstr) else left_cond,
                                         builder.load(right_cond) if isinstance(right_cond,
                                                                                ir.AllocaInstr) else right_cond)
        builder.cbranch(for_cond, for_body_block, exit_block)
        builder.position_at_end(exit_block)

    def if_statement(self, stat: dict, builder=None):
        builder = builder if builder else self.builder
        if_statement = stat['ifStatement']
        condition = if_statement['condition']
        if_body = if_statement['body']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if function_name != 'main' else self.main_func

        cond_l = condition['left']
        cond_r = condition['right']

        left_cond = self.evaluate_expression(cond_l, builder)
        right_cond = self.evaluate_expression(cond_r, builder)

        if cond_l['type'] == 'VAR' and left_cond.function != func:
            left_cond = {'type': "VAR", 'value': cond_l['value'] + '_tmp'}
            left_cond = self.evaluate_expression(left_cond, builder)

        if cond_r['type'] == 'VAR' and right_cond.function != func:
            right_cond = {'type': "VAR", 'value': cond_r['value'] + '_tmp'}
            right_cond = self.evaluate_expression(right_cond, builder)

        left_cond = builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond
        right_cond = builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond

        left_cond = builder.load(left_cond) if isinstance(left_cond.type, ir.PointerType) else left_cond
        right_cond = builder.load(right_cond) if isinstance(right_cond.type, ir.PointerType) else right_cond
        op = condition['op']

        if isinstance(left_cond.type, ir.DoubleType) and isinstance(right_cond.type, ir.IntType):
            right_cond = builder.sitofp(right_cond, left_cond.type)
        elif isinstance(right_cond.type, ir.DoubleType) and isinstance(left_cond.type, ir.IntType):
            left_cond = builder.sitofp(left_cond, right_cond.type)
        if isinstance(left_cond.type, ir.DoubleType) and isinstance(right_cond.type, ir.DoubleType):
            if_cond = builder.fcmp_ordered(op, left_cond, right_cond)
        else:
            if_cond = builder.icmp_signed(op, left_cond, right_cond)

        then_block = func.append_basic_block(name="if.then")
        end_block = func.append_basic_block(name="if.end")

        builder.cbranch(if_cond, then_block, end_block)

        builder.position_at_start(then_block)

        self.item_bypass(if_body, builder)

        builder.branch(end_block)
        builder.position_at_start(end_block)

    def if_else_statement(self, stat: dict, builder=None):
        builder = builder if builder else self.builder
        if_else_statement = stat['ifElseStatement']
        condition = if_else_statement['condition']
        if_body = if_else_statement['ifBody']
        if_else_body = if_else_statement['elseBody']
        function_name = builder.function.name
        func = self.functions[function_name]['func'] if function_name != 'main' else self.main_func

        cond_l = condition['left']
        cond_r = condition['right']

        left_cond = self.evaluate_expression(cond_l, builder)
        right_cond = self.evaluate_expression(cond_r, builder)

        if cond_l['type'] == 'VAR' and left_cond.function != func:
            left_cond = {'type': "VAR", 'value': cond_l['value'] + '_tmp'}
            left_cond = self.evaluate_expression(left_cond, builder)

        if cond_r['type'] == 'VAR' and right_cond.function != func:
            right_cond = {'type': "VAR", 'value': cond_r['value'] + '_tmp'}
            right_cond = self.evaluate_expression(right_cond, builder)

        left_cond = builder.load(left_cond) if isinstance(left_cond, ir.AllocaInstr) else left_cond
        right_cond = builder.load(right_cond) if isinstance(right_cond, ir.AllocaInstr) else right_cond

        left_cond = builder.load(left_cond) if isinstance(left_cond.type, ir.PointerType) else left_cond
        right_cond = builder.load(right_cond) if isinstance(right_cond.type, ir.PointerType) else right_cond

        op = condition['op']

        if isinstance(left_cond.type, ir.DoubleType) and isinstance(right_cond.type, ir.IntType):
            right_cond = builder.sitofp(right_cond, left_cond.type)
        elif isinstance(right_cond.type, ir.DoubleType) and isinstance(left_cond.type, ir.IntType):
            left_cond = builder.sitofp(left_cond, right_cond.type)
        if isinstance(left_cond.type, ir.DoubleType) and isinstance(right_cond.type, ir.DoubleType):
            if_cond = builder.fcmp_ordered(op, left_cond, right_cond)
        else:
            if_cond = builder.icmp_signed(op, left_cond, right_cond)

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
            if value == 'double':
                double_type = ir.DoubleType()
                global_var = ir.GlobalVariable(self.module, double_type, item)
                global_var.initializer = ir.Constant(double_type, 0.0)
                self.variables[item] = global_var

    def function_statement(self, statement):
        func_statement = statement["functionStatement"]
        args = func_statement['args']
        func_name = func_statement['name']
        func_body = func_statement['body']
        f_type = func_statement["type"]
        type_entry = self.choose_type_entry[f_type]

        func_type = ir.FunctionType(type_entry, [self.choose_type_entry[arg] for key, arg in args.items()])
        func = ir.Function(self.module, func_type, name=func_name)
        block = func.append_basic_block(name='entry')
        builder = ir.IRBuilder(block)
        self.functions[func_name] = {"builder": builder, "func": func}

        for arg, var_name in zip(func.args, args.keys()):
            var = builder.alloca(self.choose_type_entry[args[var_name]], name=f"{var_name}_tmp")
            builder.store(arg, var)
            self.variables[f"{var_name}_tmp"] = {"var": var, "func": builder.function.name}

        self.item_bypass(func_body, builder)

        if f_type == 'void':
            self.functions[func_name]['builder'].ret_void()

    def function_call(self, stat: dict, builder=None):
        builder = builder if builder is not None else self.builder
        function_name = stat['functionCall']['name']
        function_type = stat['functionCall']['type']
        function_args = stat['functionCall']['params']

        func = self.functions[function_name]

        expected_types = [arg.type for arg in func['func'].args]

        params = []
        for i, arg in enumerate(function_args):
            if arg in self.variables:
                var_info = self.variables[arg]
                arg_type = var_info['var'].type.pointee
                if arg_type == expected_types[i]:
                    params.append(builder.load(var_info['var']))
                else:
                    try:
                        raise TypeError(f"Аргумент {i} должен быть типом '{expected_types[i]}', а не '{arg_type}'")
                    except TypeError as e:
                        print(str(e))
                        sys.exit(1)

            elif isinstance(expected_types[i], ir.IntType):
                try:
                    arg = int(arg)
                except ValueError:
                    try:
                        raise ValueError(f"Аргумент {i} должен быть типа 'int', а не 'double'")
                    except ValueError as e:
                        print(str(e))
                        sys.exit(1)
                finally:
                    params.append(ir.Constant(ir.IntType(32), arg))

            elif isinstance(expected_types[i], ir.DoubleType):
                try:
                    arg = float(arg)
                    if arg.is_integer():
                        try:
                            raise ValueError(f"Аргумент {i} должен быть типа 'double'")
                        except ValueError as e:
                            print(str(e))
                            sys.exit(1)
                finally:
                    params.append(ir.Constant(ir.DoubleType(), arg))

        if function_type == 'void':
            self.builder.call(func['func'], params)
        elif function_type == 'int':
            self.builder.call(func['func'], params)

    def return_statement(self, stat, builder=None):
        builder = builder if builder is not None else self.builder
        return_ = stat['return']['value']
        func_name = builder.function.name

        if builder.block.is_terminated:

            return
        elif isinstance(builder.function.ftype.return_type, ir.VoidType):
            self.functions[func_name]['builder'].ret_void()
        elif isinstance(builder.function.ftype.return_type, ir.IntType):
            try:
                self.functions[func_name]['builder'].ret(ir.Constant(ir.IntType(32), int(return_)))
            except:
                self.functions[func_name]['builder'].ret(builder.load(self.variables[return_]['var']))

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
            elif 'return' in item:
                self.return_statement(item)

        self.builder.ret_void()


def translate_to_llvm():
    tolvm = TranslatorToLLVM()
    tolvm.json_reader()
    tolvm.builder_init()
    tolvm.ast_bypass()
    tolvm.ll_writer()
    # print(tolvm.variables)
    # print("Промежуточный код готов!")


if __name__ == "__main__":
    translate_to_llvm()
