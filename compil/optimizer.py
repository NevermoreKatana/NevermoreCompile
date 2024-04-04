import os
import sys
import math
current_directory = os.getcwd()
sys.path.insert(0, current_directory)

from llvmlite import binding
from compil.mixins import ReadWriteMixin
import re


class NeplAstOptimizer(ReadWriteMixin):
    def __init__(self, ast_file) -> None:
        self.ast_reader(ast_file)

    def check_for_var(self, expr):

        if 'type' in expr and expr['type'] == 'VAR' or 'functionCall' in expr:
            return False
        elif 'type' in expr and expr['type'] in ['ADD', 'SUB', 'MUL', 'DIV', 'POW']:
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
        elif 'type' in expr and expr['type'] == 'POW':
            return math.pow(self.calculate(expr['left']), self.calculate(expr['right']))

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


def ast_optimizer(ast_file):
    opt = NeplAstOptimizer(ast_file)
    opt.traverse(opt.ast)
    opt.ast_writer(ast_file)
