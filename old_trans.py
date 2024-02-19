import llvmlite.ir as ir
import json


choose_type_entry = {
    "void": ir.VoidType(),
    "int": ir.IntType(32)
}


class ToLlvmCode:
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

    def json_reader(self, input_file="output_files/ast.json"):
        with open(input_file, "r") as f:
            self.ast = json.load(f)

    def ll_writer(self, output_file="output_files/output.ll"):
        with open(output_file, "w") as f:
            f.write(str(self.module))

    def builder_init(self):
        main_func_type = ir.FunctionType(ir.VoidType(), [])
        main_func = ir.Function(self.module, main_func_type, name="main")
        self.main_func = main_func
        block = main_func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        self.builder = builder
        return

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

    def g_const_print_stroke_format(self):
        stroke_str = "stroke\0"
        stroke_str_ptr = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(stroke_str)),
                                           name=".str.stroke")
        stroke_str_ptr.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(stroke_str)),
                                                 bytearray(stroke_str.encode()))
        self.format_str_loaded_str = stroke_str_ptr

    def evaluate_expression(self, expr, builder):
        if expr['type'] == 'INT' or expr['type'] == 'int':
            return ir.Constant(ir.IntType(32), expr['value'])
        elif expr['type'] == 'ID':
            return self.variables[expr['value']]
        elif expr['type'] in ['DIV', 'MUL', 'ADD', 'SUB']:
            return self.execute_math_operation(expr, builder)
        else:
            raise ValueError(f"Unsupported expression type: {expr['type']}")

    def execute_math_operation(self, expr, builder):
        left_value = self.evaluate_expression(expr['left'], builder)
        right_value = self.evaluate_expression(expr['right'], builder)
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

    def assign_statement(self, statement):
        assignment = statement['assignmentStatement']
        var_name = assignment['ID']
        expr = assignment['expr'][0]

        value = self.evaluate_expression(expr, self.builder)

        if var_name in self.variables:
            var = self.variables[var_name]
        else:
            var = self.builder.alloca(ir.IntType(32), name=var_name)
            self.variables[var_name] = var
        self.builder.store(value, var)

    def while_statement(self, statement):
        while_statement = statement['whileStatement']
        condition = while_statement['condition']
        while_body = while_statement['body']

        left_value = self.evaluate_expression(condition['left'], self.builder)
        right_value = self.evaluate_expression(condition['right'], self.builder)
        left_id = condition['left_ID']
        right_id = condition['right_ID']
        op = condition['op']

        while_block = self.main_func.append_basic_block(name="while")
        end_block = self.main_func.append_basic_block(name="end")

        cond = self.builder.icmp_unsigned(op, self.builder.load(self.variables[left_id]),
                                          right_value)
        self.builder.cbranch(cond, while_block, end_block)

        self.builder.position_at_end(while_block)

        for stat_item in while_body:
            if 'stat' in stat_item:
                stat = stat_item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat, self.builder)
                elif 'assignmentStatement' in stat:
                    self.assign_statement(stat)
            elif 'ifStatement' in stat_item:
                self.if_statement(stat_item)
            elif 'ifElseStatement' in stat_item:
                self.if_else_statement(stat_item)
            elif 'forStatement' in stat_item:
                self.for_statement(stat_item)
            elif 'whileStatement' in stat_item:
                self.while_statement(stat_item)
            elif 'doWhileStatement' in stat_item:
                self.do_while_statement(stat_item)

        inc_i = self.builder.add(self.builder.load(self.variables[left_id]), ir.Constant(ir.IntType(32), 1))
        self.builder.store(inc_i, self.variables[left_id])
        cond = self.builder.icmp_unsigned(op, self.builder.load(self.variables[left_id]),
                                          right_value)

        self.builder.cbranch(cond, while_block, end_block)

        self.builder.position_at_end(end_block)

    def print_statement(self, statement, builder=None):
        print_statement = statement['printStatement']
        expr = print_statement['expr']

        value = self.evaluate_expression(expr, builder)
        self.choose_print_type(value, builder if builder else None)

    def choose_print_type(self, value, builder = None):
        builder = builder if builder else self.builder
        if isinstance(value, ir.AllocaInstr):
            value = f'%"{builder.load(value).name}"'
        builder.call(self.print_func, [self.format_str_loaded_int, ir.Constant(ir.IntType(32), value)])

    def globalStatement(self, statement):
        for item, value in statement.items():
            if value == 'int':
                int_type = ir.IntType(32)
                global_var = ir.GlobalVariable(self.module, int_type, item)
                global_var.initializer = ir.Constant(int_type, 0)
                self.variables[item] = global_var

    def do_while_statement(self, statement):
        do_while_statement = statement['doWhileStatement']
        while_body = do_while_statement['body']
        do_body = do_while_statement['do']

        left_value = self.evaluate_expression(do_body['left'])
        right_value = self.evaluate_expression(do_body['right'])
        left_id = do_body['left_ID']
        right_id = do_body['right_ID']
        op = do_body['op']

        loop_start_block = self.main_func.append_basic_block(name="loop_start")
        loop_body_block = self.main_func.append_basic_block(name="loop_body")
        loop_end_block = self.main_func.append_basic_block(name="loop_end")

        self.builder.branch(loop_start_block)
        self.builder.position_at_end(loop_start_block)

        for stat_item in while_body:
            if 'stat' in stat_item:
                stat = stat_item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat)
                elif 'assignmentStatement' in stat:
                    self.assign_statement(stat)
            elif 'ifStatement' in stat_item:
                self.if_statement(stat_item)
            elif 'ifElseStatement' in stat_item:
                self.if_else_statement(stat_item)
            elif 'forStatement' in stat_item:
                self.for_statement(stat_item)
            elif 'whileStatement' in stat_item:
                self.while_statement(stat_item)
            elif 'doWhileStatement' in stat_item:
                self.do_while_statement(stat_item)

        loop_condition = self.builder.load(self.variables[left_id])
        cond = self.builder.icmp_unsigned(op, loop_condition, ir.Constant(ir.IntType(32), right_value))
        self.builder.cbranch(cond, loop_body_block, loop_end_block)

        self.builder.position_at_end(loop_body_block)

        # Здесь можно добавить инструкции, которые должны выполняться после тела цикла

        inc_i = self.builder.add(self.builder.load(self.variables[left_id]), ir.Constant(ir.IntType(32), 1))
        self.builder.store(inc_i, self.variables[left_id])

        exit_condition = self.builder.icmp_unsigned(op, inc_i, ir.Constant(ir.IntType(32), right_value))
        self.builder.branch(loop_start_block)

        self.builder.position_at_end(loop_end_block)


    def function_statement(self, statement):
        func_statement = statement["functionStatement"]
        func_name  = func_statement['name']
        type_entry = choose_type_entry[func_statement["type"]]

        func_type = ir.FunctionType(type_entry, [])
        func = ir.Function(self.module, func_type, name=func_name)
        block = func.append_basic_block(name='entry')
        builder = ir.IRBuilder(block)
        self.functions[func_name] = builder
        self.builder.call(func, [])

        for item in func_statement['body']:
            if 'stat' in item:
                stat = item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat, builder)
        return

    def if_statement(self, item):
        if_statement = item['ifStatement']
        condition = if_statement['condition']
        body = if_statement['body']

        left_value = self.evaluate_expression(condition['left'])
        right_value = self.evaluate_expression(condition['right'])
        llvm_condition = self.builder.icmp_signed(condition['op'], ir.Constant(ir.IntType(32), left_value),
                                                  ir.Constant(ir.IntType(32), right_value))
        then_block = self.main_func.append_basic_block(name="if.then")
        merge_block = self.main_func.append_basic_block(name="if.end")

        self.builder.cbranch(llvm_condition, then_block, merge_block)

        self.builder.position_at_start(then_block)
        for stat_item in body:
            if 'stat' in stat_item:
                stat = stat_item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat)
                elif 'assignmentStatement' in stat:
                    self.assign_statement(stat)
            elif 'ifStatement' in stat_item:
                self.if_statement(stat_item)
            elif 'ifElseStatement' in stat_item:
                self.if_else_statement(stat_item)
            elif 'forStatement' in stat_item:
                self.for_statement(stat_item)
            elif 'whileStatement' in stat_item:
                self.while_statement(stat_item)
            elif 'doWhileStatement' in stat_item:
                self.do_while_statement(stat_item)


        self.builder.branch(merge_block)

        self.builder.position_at_start(merge_block)

    def if_else_statement(self, statement):
        if_else_statement = statement['ifElseStatement']
        condition = if_else_statement['condition']
        if_body = if_else_statement['ifBody']
        else_body = if_else_statement['elseBody']

        left_value = self.evaluate_expression(condition['left'])
        right_value = self.evaluate_expression(condition['right'])
        llvm_condition = self.builder.icmp_signed(condition['op'], ir.Constant(ir.IntType(32), left_value),
                                                  ir.Constant(ir.IntType(32), right_value))
        then_block = self.main_func.append_basic_block(name="if_else.then")
        else_block = self.main_func.append_basic_block(name="if_else.else")
        merge_block = self.main_func.append_basic_block(name="if_else.end")

        self.builder.cbranch(llvm_condition, then_block, else_block)

        self.builder.position_at_start(then_block)
        for stat_item in if_body:
            if 'stat' in stat_item:
                stat = stat_item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat)
                elif 'assignmentStatement' in stat:
                    self.assign_statement(stat)
            elif 'ifStatement' in stat_item:
                self.if_statement(stat_item)
            elif 'ifElseStatement' in stat_item:
                self.if_else_statement(stat_item)
            elif 'forStatement' in stat_item:
                self.for_statement(stat_item)
            elif 'whileStatement' in stat_item:
                self.while_statement(stat_item)
            elif 'doWhileStatement' in stat_item:
                self.do_while_statement(stat_item)

        self.builder.branch(merge_block)

        self.builder.position_at_start(else_block)
        for stat_item in else_body:
            if 'stat' in stat_item:
                stat = stat_item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat)
                elif 'assignmentStatement' in stat:
                    self.assign_statement(stat)
            elif 'ifStatement' in stat_item:
                self.if_statement(stat_item)
            elif 'ifElseStatement' in stat_item:
                self.if_else_statement(stat_item)
            elif 'forStatement' in stat_item:
                self.for_statement(stat_item)
            elif 'whileStatement' in stat_item:
                self.while_statement(stat_item)
            elif 'doWhileStatement' in stat_item:
                self.do_while_statement(stat_item)
        self.builder.branch(merge_block)

        self.builder.position_at_start(merge_block)



    def for_statement(self, statement):
        for_statement = statement['forStatement']
        for_init = for_statement['init']
        condition = for_statement['condition']
        modify = for_statement['modify']
        for_body = for_statement['body']

        for_var_name = for_init['stat']['assignmentStatement']['ID']
        left_value = self.evaluate_expression(condition['left'])
        right_value = self.evaluate_expression(condition['right'])
        op = condition['op']

        if 'stat' in for_init:
            stat = for_init['stat']
            if 'assignmentStatement' in stat:
                self.assign_statement(stat)

        loop_body_block = self.main_func.append_basic_block(name="loop_body")
        exit_block = self.main_func.append_basic_block(name="exit")
        loop_cond = self.builder.icmp_unsigned(op, self.builder.load(self.variables[for_var_name]),
                                               ir.Constant(ir.IntType(32), right_value))

        self.builder.cbranch(loop_cond, loop_body_block, exit_block)

        self.builder.position_at_start(loop_body_block)
        for stat_item in for_body:
            if 'stat' in stat_item:
                stat = stat_item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat)
                elif 'assignmentStatement' in stat:
                    self.assign_statement(stat)
            elif 'ifStatement' in stat_item:
                self.if_statement(stat_item)
            elif 'ifElseStatement' in stat_item:
                self.if_else_statement(stat_item)
            elif 'forStatement' in stat_item:
                self.for_statement(stat_item)
            elif 'whileStatement' in stat_item:
                self.while_statement(stat_item)
            elif 'doWhileStatement' in stat_item:
                self.do_while_statement(stat_item)

        new_i_value = self.builder.add(self.builder.load(self.variables[for_var_name]), ir.Constant(ir.IntType(32), 1))
        self.builder.store(new_i_value, self.variables[for_var_name])

        loop_cond = self.builder.icmp_unsigned(op, self.builder.load(self.variables[for_var_name]),
                                               ir.Constant(ir.IntType(32), right_value))
        self.builder.cbranch(loop_cond, loop_body_block, exit_block)

        self.builder.position_at_start(exit_block)

    def AST_bypass(self):
        for item in self.ast:
            if 'globalStatement' in item:
                self.globalStatement(item['globalStatement'])

            if 'stat' in item :
                stat = item['stat']

                if 'assignmentStatement' in stat:
                    self.assign_statement(stat)
                elif 'printStatement' in stat:
                    self.print_statement(stat)
            elif 'ifStatement' in item:
                self.if_statement(item)
            elif 'ifElseStatement' in item:
                self.if_else_statement(item)
            elif 'forStatement' in item:
                self.for_statement(item)
            elif 'whileStatement' in item:
                self.while_statement(item)
            elif 'doWhileStatement' in item:
                self.do_while_statement(item)
            elif 'functionStatement' in item:
                if item['functionStatement']['name'] not in self.functions:
                    self.function_statement(item)


        self.builder.ret_void()


    def __str__(self):
        return str(self.module)




if __name__ == '__main__':
    tolvm = ToLlvmCode()
    tolvm.json_reader()
    tolvm.builder_init()
    tolvm.g_const_print_int_format()
    tolvm.AST_bypass()
    tolvm.ll_writer()
    print("Промежуточный код готов!")