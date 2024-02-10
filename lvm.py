import llvmlite.ir as ir
import json


class ToLlvmCode:
    def __init__(self):
        self.module = ir.Module("nevermoreCompile")
        self.ast = None
        self.print_func = None
        self.builder = None
        self.format_str_loaded_int = None
        self.format_str_loaded_str = None
        self.variables = {}
        self.main_func = None
        #Init func
        self.builder_init()
        self.g_const_print_int_format()
        # self.g_const_print_stroke_format()
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


    def evaluate_expression(self, expr):
        if expr['type'] == 'INT' or expr['type'] == 'int':
            return expr['value']
        elif expr['type'] == 'DIV':
            left_value = self.evaluate_expression(expr['left'])
            right_value = self.evaluate_expression(expr['right'])
            return int(left_value / right_value)
        elif expr['type'] == 'MUL':
            left_value = self.evaluate_expression(expr['left'])
            right_value = self.evaluate_expression(expr['right'])
            return int(left_value * right_value)
        elif expr['type'] == 'ADD':
            left_value = self.evaluate_expression(expr['left'])
            right_value = self.evaluate_expression(expr['right'])
            return left_value + right_value
        elif expr['type'] == 'SUB':
            left_value = self.evaluate_expression(expr['left'])
            right_value = self.evaluate_expression(expr['right'])
            return left_value - right_value
        else:
            raise ValueError(f"Unsupported expression type: {expr['type']}")
    def assign_statement(self, statement):
        assignment = statement['assignmentStatement']
        var_name = assignment['ID']
        expr = assignment['expr'][0]

        value = self.evaluate_expression(expr)
        var = self.builder.alloca(ir.IntType(32), name=var_name)
        self.builder.store(ir.Constant(ir.IntType(32), value), var)
        self.variables[var_name] = var

    def print_statement(self, statement):
        print_statement = statement['printStatement']
        expr = print_statement['expr']

        value = self.evaluate_expression(expr)
        self.choose_print_type(value, expr['type'])

    def choose_print_type(self, value, data_type):
        self.builder.call(self.print_func, [self.format_str_loaded_int, ir.Constant(ir.IntType(32), value)])

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

        self.builder.branch(merge_block)

        self.builder.position_at_start(else_block)
        for stat_item in else_body:
            if 'stat' in stat_item:
                stat = stat_item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat)
                elif 'assignmentStatement' in stat:
                    self.assign_statement(stat)
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

        new_i_value = self.builder.add(self.builder.load(self.variables[for_var_name]), ir.Constant(ir.IntType(32), 1))
        self.builder.store(new_i_value, self.variables[for_var_name])

        loop_cond = self.builder.icmp_unsigned(op, self.builder.load(self.variables[for_var_name]),
                                               ir.Constant(ir.IntType(32), right_value))
        self.builder.cbranch(loop_cond, loop_body_block, exit_block)

        self.builder.position_at_start(exit_block)

    def while_statement(self, statement):
        while_statement = statement['whileStatement']
        condition = while_statement['condition']
        while_body = while_statement['body']

        left_value = self.evaluate_expression(condition['left'])
        right_value = self.evaluate_expression(condition['right'])
        left_id = condition['left_ID']
        right_id = condition['right_ID']
        op = condition['op']

        while_block = self.main_func.append_basic_block(name="while")
        end_block = self.main_func.append_basic_block(name="end")

        cond = self.builder.icmp_unsigned(op, self.builder.load(self.variables[left_id]),
                                        ir.Constant(ir.IntType(32), right_value))
        self.builder.cbranch(cond, while_block, end_block)

        self.builder.position_at_end(while_block)

        for stat_item in while_body:
            if 'stat' in stat_item:
                stat = stat_item['stat']
                if 'printStatement' in stat:
                    self.print_statement(stat)
                elif 'assignmentStatement' in stat:
                    self.assign_statement(stat)

        inc_i = self.builder.add(self.builder.load(self.variables[left_id]), ir.Constant(ir.IntType(32), 1))
        self.builder.store(inc_i, self.variables[left_id])
        cond = self.builder.icmp_unsigned(op, self.builder.load(self.variables[left_id]),
                                        ir.Constant(ir.IntType(32), right_value))

        self.builder.cbranch(cond, while_block, end_block)

        self.builder.position_at_end(end_block)

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

    def tree_bypass(self):
        for item in self.ast:
            if 'stat' in item:
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


        self.builder.ret_void()


    def __str__(self):
        return str(self.module)




if __name__ == '__main__':
    tolvm = ToLlvmCode()
    tolvm.json_reader()
    tolvm.tree_bypass()
    tolvm.ll_writer()
    print("Промежуточный код готов!")