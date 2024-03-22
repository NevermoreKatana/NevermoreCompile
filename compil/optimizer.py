import os
import sys
import struct

current_directory = os.getcwd()
sys.path.insert(0, current_directory)

from llvmlite import ir, binding
from compil.mixins import ReadWriteMixin
import re
pattern = r' (add|sub|mul|udiv|fdiv|fadd|fmul|fsub) (i32|double) (0x[0-9a-fA-F]+|\d+), (0x[0-9a-fA-F]+|\d+)'
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


class NeplOptimizer:
    def __init__(self, input_file) -> None:
        self.module = ir.Module("nevermoreCompile")
        self.module.triple = 'x86_64-pc-linux-gnu'
        self.ll_file = self.reader(input_file)
        self.builder_init()
        
    def reader(self, filename):
        with open(filename, 'r') as f:
            return f.read()
    
    def builder_init(self) -> None:
        func_name = 'main'
        func_type = ir.VoidType()

        main_func_type = ir.FunctionType(func_type, [])
        main_func = ir.Function(self.module, main_func_type, name=func_name)
        self.main_func = main_func
        block = main_func.append_basic_block(name=f"entry.{func_name}")
        builder = ir.IRBuilder(block)
        self.builder = builder
    
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
    
    def add(self, line):
        if self.data_type == 'i32':
            result = int(int(self.num1) + int(self.num2))
            
            line1 = f'  %"{self.var_name}" = alloca i32'
            line2 = f'  store i32 {result}, i32* %"{self.var_name}"'
            line3 = '' if 'store' in line else line
            return line1, line2, line3

        if self.data_type == 'double':
            num1, num2 = self.hex_from_str(self.num1, self.num2)
            result = float(float(num1) + float(num2))
            
            line1 = f'  %"{self.var_name}" = alloca double'
            line2 = f'  store double {result}, double* %"{self.var_name}"'
            line3 = '' if 'store' in line else line
            return line1, line2, line3
        
    def sub(self,line):
        if self.data_type == 'i32':
            result = int(int(self.num1) - int(self.num2))
            
            line1 = f'  %"{self.var_name}" = alloca i32'
            line2 = f'  store i32 {result}, i32* %"{self.var_name}"'
            line3 = '' if 'store' in line else line
            return line1, line2, line3

        if self.data_type == 'double':
            num1, num2 = self.hex_from_str(self.num1, self.num2)
            result = float(float(num1) - float(num2))
            
            line1 = f'  %"{self.var_name}" = alloca double'
            line2 = f'  store double {result}, double* %"{self.var_name}"'
            line3 = '' if 'store' in line else line
            return line1, line2, line3
        
    def div(self,line):
        if self.data_type == 'i32':
            result = int(int(self.num1) / int(self.num2))
            
            line1 = f'  %"{self.var_name}" = alloca i32'
            line2 = f'  store i32 {result}, i32* %"{self.var_name}"'
            line3 = '' if 'store' in line else line
            return line1, line2, line3

        if self.data_type == 'double':
            num1, num2 = self.hex_from_str(self.num1, self.num2)
            result = float(float(num1) / float(num2))
            
            line1 = f'  %"{self.var_name}" = alloca double'
            line2 = f'  store double {result}, double* %"{self.var_name}"'
            line3 = '' if 'store' in line else line
            return line1, line2, line3
    
    def mul(self, line):
        if self.data_type == 'i32':
            result = int(int(self.num1) * int(self.num2))
            
            line1 = f'  %"{self.var_name}" = alloca i32'
            line2 = f'  store i32 {result}, i32* %"{self.var_name}"'
            line3 = '' if 'store' in line else line
            return line1, line2, line3

        if self.data_type == 'double':
            num1, num2 = self.hex_from_str(self.num1, self.num2)
            result = float(float(num1) * float(num2))
            
            line1 = f'  %"{self.var_name}" = alloca double'
            line2 = f'  store double {result}, double* %"{self.var_name}"'
            line3 = '' if 'store' in line else line
            return line1, line2, line3
        
        
    def math_operands(self):
        lines = self.ll_file.split('\n')
        self.ll_file = ''
        for i in range(len(lines)):
            line = lines[i]
            matches = re.finditer(pattern, line)

            for match in matches:
                operation, self.data_type, self.num1, self.num2 = match.groups()
                self.var_name = lines[i+1]
                self.var_name = re.search(r'"([a-zA-Zа-яА-Я][a-zA-Zа-яА-Я0-9]*)"', self.var_name).group(1) if re.search(r'"([a-zA-Zа-яА-Я][a-zA-Zа-яА-Я0-9]*)"', self.var_name) else None

                
                if operation in ['add', 'fadd'] and self.var_name is not None:
                    lines[i],lines[i+1], lines[i+2]  = self.add(lines[i+2])
                if operation in ['sub', 'fsub']and self.var_name is not None:
                    lines[i],lines[i+1], lines[i+2] = self.sub(lines[i+2])
                if operation in ['mul', 'fmul']and self.var_name :
                    lines[i],lines[i+1], lines[i+2] = self.mul(lines[i+2])

        self.ll_file = '\n'.join(lines)

    
    def write(self, filename):
        with open(filename, 'w') as f:
            f.write(self.ll_file)

    def __str__(self) -> str:
        return str(self.ll_file)
def optimize_ll(ll_output_file: str = None, ll_optimize_file: str = None) -> None:
    try:
        print("First optimization\nDeleting math operations")
        optimzer1 = NeplOptimizer(ll_output_file)
        optimzer1.math_operands()
        optimzer1.write(ll_optimize_file)
        print("Second optimization")
        optimzer = Optimizer(ll_optimize_file)
        optimzer.optimize()
        optimzer.ll_writer(ll_optimize_file)
    except:
        optimzer = Optimizer(ll_output_file)
        optimzer.optimize()
        optimzer.ll_writer(ll_optimize_file)

