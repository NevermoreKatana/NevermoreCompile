import os
import sys
import struct

current_directory = os.getcwd()
sys.path.insert(0, current_directory)

from llvmlite import ir, binding
from compil.mixins import ReadWriteMixin
import re
pattern = r'(add|sub|mul|udiv|fdiv|fadd|fmul|fsub) (i32|double) (0x[0-9a-fA-F]+|\d+), (0x[0-9a-fA-F]+|\d+)'
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


class MyOptimizer(ReadWriteMixin):
        
    def __init__(self, filename) -> None:
        self.module = ir.Module("nevermoreCompile")
        self.module.triple = 'x86_64-pc-linux-gnu'
        self.variables = {}
        self.functions = {}
        self.ll_file = filename
        self.ll_reader()
        self.optimized_file = None
        self.init_opt_file()
        
    def init_opt_file(self):
       
        func_name = 'main'
        func_type = ir.VoidType()

        main_func_type = ir.FunctionType(func_type, [])
        main_func = ir.Function(self.module, main_func_type, name=func_name)
        self.main_func = main_func
        block = main_func.append_basic_block(name=f"entry.{func_name}")
        builder = ir.IRBuilder(block)
        self.builder = builder
        self.functions[func_name] = builder
        
    def hex_from_str(self, num1, num2):
        if num1.startswith('0x'):
            num1 = num1[2:]
        if num2.startswith('0x'):
            num2 = num2[2:]
        
        num1 = bytes.fromhex(num1)
        num1 = struct.unpack('!d', num1)[0]

        num2 = bytes.fromhex(num2)       
        num2 = struct.unpack('!d', num2)[0]
        
        return num1, num2
    def math_operands(self):
        lines = self.ll_file.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            matches = re.findall(pattern, line)

            if matches:
                for match in matches:
                    operation, data_type, num1, num2 = match
                    var_name = lines[i+1]
                    var_name = re.search(r'"([^"]*)"', var_name).group(1)
                    if operation in ['add', 'fadd']:
                        if data_type == 'i32':
                            result = int(int(num1) + int(num2))
                            
                            lines[i] = f'\t%"{var_name}" = alloca i32'
                            lines[i+1] = f'\tstore i32 {result}, i32* %"{var_name}"'
                            lines[i+2] = ''

                        if data_type == 'double':
                            num1, num2 = self.hex_from_str(num1, num2)
                            result = float(float(num1) + float(num2))
                            
                            lines[i] = f'\t%"{var_name}" = alloca double'
                            lines[i+1] = f'store double {result}, double* %"{var_name}"'
                            lines[i+2] = ''

                    elif operation in ['sub', 'fsub']:
                        if data_type == 'i32':
                            result = int(int(num1) - int(num2))
                            lines[i] = f'\t%"{var_name}" = alloca i32'
                            lines[i+1] = f'\tstore i32 {result}, i32* %"{var_name}"'
                            lines[i+2] = ''

                        if data_type == 'double':
                            num1, num2 = self.hex_from_str(num1, num2)
                            result = float(float(num1) - float(num2))
                            lines[i] = f'\t%"{var_name}" = alloca double'
                            lines[i+1] = f'\tstore double {result}, double* %"{var_name}"'
                            lines[i+2] =''

        self.ll_file = '\n'.join(lines)
    
    def write(self, filename):
        with open(filename, 'w') as f:
            f.write(self.ll_file)


def optimize_ll(ll_output_file: str = None, ll_optimize_file: str = None) -> None:
    # optimzer1 = MyOptimizer(ll_output_file)
    # optimzer1.math_operands()
    # optimzer1.write(ll_optimize_file)
    optimzer = Optimizer(ll_output_file)
    optimzer.optimize()
    optimzer.ll_writer(ll_optimize_file)








# opt = MyOptimizer('compil/outpit_files/output.ll')

# opt.math_operands()
