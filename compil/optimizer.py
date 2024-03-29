import os
import sys

current_directory = os.getcwd()
sys.path.insert(0, current_directory)

from llvmlite import ir, binding
from compil.mixins import ReadWriteMixin
import re


class Optimizer(ReadWriteMixin):
    def __init__(self, filename: str) -> None:
        self.ll_file = filename
        self.ll_reader()
        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()
        self.module = binding.parse_assembly(self.ll_file)

    def optimize(self) -> None:
        pass_manager = binding.create_module_pass_manager()
        # Объединяет одинаковые глобальные константы в одну
        pass_manager.add_constant_merge_pass()
        # Удаляет аргументы функций, которые не используются
        pass_manager.add_dead_arg_elimination_pass()
        # Встраивает функции, размер которых меньше или равен порогу (в данном случае 225)
        pass_manager.add_function_inlining_pass(threshold=225)
        # Удаляет неиспользуемые глобальные значения
        pass_manager.add_global_optimizer_pass()
        # Удаляет мертвый код
        pass_manager.add_dead_code_elimination_pass()
        # Упрощает управляющие графы потока для улучшения производительности
        pass_manager.add_cfg_simplification_pass()
        # Комбинирует инструкции для улучшения производительности
        pass_manager.add_instruction_combining_pass()
        # Раскручивает циклы для улучшения производительности
        pass_manager.add_loop_unroll_pass()
        # Производит межпроцедурное распространение констант и условий
        pass_manager.add_ipsccp_pass()
        # Применяет оптимизацию Global Value Numbering для устранения избыточных вычислений
        pass_manager.add_gvn_pass()
        # Выносит инварианты цикла из цикла для улучшения производительности
        pass_manager.add_licm_pass()
        # Применяет оптимизацию Sparse Conditional Constant Propagation для устранения избыточных вычислений
        pass_manager.add_sccp_pass()
        # Удаляет хвостовые вызовы для улучшения производительности
        pass_manager.add_tail_call_elimination_pass()
        pass_manager.run(self.module)


class NeplAstOptimizer(ReadWriteMixin):
    def __init__(self, ast_file) -> None:
        self.ast_reader(ast_file)

    def calculate(self, expr):
        if expr['type'] == 'INT':
            return expr['value']
        elif expr['type'] == 'DOUBLE':
            return expr['value']
        elif expr['type'] == 'ADD':
            return self.calculate(expr['left']) + self.calculate(expr['right'])
        elif expr['type'] == 'SUB':
            return self.calculate(expr['left']) - self.calculate(expr['right'])
        elif expr['type'] == 'MUL':
            return self.calculate(expr['left']) * self.calculate(expr['right'])
        elif expr['type'] == 'DIV':
            return self.calculate(expr['left']) / self.calculate(expr['right'])

    def check_for_var(self, expr):

        if 'type' in expr and expr['type'] == 'VAR':
            return False
        elif 'type' in expr and expr['type'] in ['ADD', 'SUB', 'MUL', 'DIV']:
            return self.check_for_var(expr['left']) and self.check_for_var(expr['right'])
        return True

    def calculate(self, expr):
        if 'type' in expr and expr['type'] == 'INT':
            return expr['value']
        elif 'type' in expr and expr['type'] == 'ADD':
            return self.calculate(expr['left']) + self.calculate(expr['right'])
        elif 'type' in expr and expr['type'] == 'SUB':
            return self.calculate(expr['left']) - self.calculate(expr['right'])
        elif 'type' in expr and expr['type'] == 'MUL':
            return self.calculate(expr['left']) * self.calculate(expr['right'])
        elif 'type' in expr and expr['type'] == 'DIV':
            return self.calculate(expr['left']) / self.calculate(expr['right'])

    def traverse(self, ast):
        for statement in ast:
            if 'functionStatement' in statement:
                self.traverse(statement['functionStatement']['body'])
            elif 'ifStatement' in statement:
                self.traverse(statement['ifStatement']['body'])
            elif 'stat' in statement and 'assignmentStatement' in statement['stat']:
                if self.check_for_var(statement['stat']['assignmentStatement']['expr'][0]):
                    if statement['stat']['assignmentStatement']['type'] == 'int':
                        value = self.calculate(statement['stat']['assignmentStatement']['expr'][0])
                        if value is not None:
                            statement['stat']['assignmentStatement']['expr'] = [{"type": "INT", "value": int(value)}]

                    if statement['stat']['assignmentStatement']['type'] == 'double':
                        value = self.calculate(statement['stat']['assignmentStatement']['expr'][0])
                        if value is not None:
                            statement['stat']['assignmentStatement']['expr'] = [
                                {"type": "DOUBLE", "value": float(value)}]


class NeplLOptimizer(ReadWriteMixin):
    def __init__(self, ll_file, optimize_file) -> None:
        self.ll_file = ll_file
        self.ll_reader()
        self.module = self.ll_file

    def function_optimizer(self):
        regex = r"(define (i32|void) @\"(.*)\"\(.*\)\n\{([^}]*)\}\n)"
        matches = re.finditer(regex, self.module, re.MULTILINE)

        for match in matches:
            function_text = match.group(1)
            function_name = match.group(3)

            if function_name == 'main':
                continue

            call_regex = fr"call (i32|void) @\"{function_name}\""
            matches_call = list(re.finditer(call_regex, self.module, re.MULTILINE))

            if matches_call == []:
                self.module = self.module.replace(function_text, '')


def optimize_ll(ll_output_file: str = None, ll_optimize_file: str = None) -> None:
    f_opt = NeplLOptimizer(ll_output_file, ll_optimize_file)
    f_opt.function_optimizer()
    f_opt.ll_writer(ll_optimize_file)
    optimzer = Optimizer(ll_optimize_file)
    optimzer.optimize()
    optimzer.ll_writer(ll_optimize_file)


def ast_optimizer(ast_file):
    opt = NeplAstOptimizer(ast_file)
    opt.traverse(opt.ast)
    opt.ast_writer(ast_file)
