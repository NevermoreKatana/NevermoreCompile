from llvmlite import ir, binding
from ini import *


class Optimizer():
    def __init__(self, filename: str, outputfile: str) -> None:
        self.ll_file = filename
        self.output_file = outputfile
        self.reader()
        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()
        self.module = binding.parse_assembly(self.ll_file)

    def reader(self):
        with open(self.ll_file, 'r') as f:
            self.ll_file = f.read()

    def writer(self):
        with open(self.output_file, 'w') as f:
            f.write(str(self.module))

    def optimize(self):
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


def optimize_ll():
    optimzer = Optimizer(ll_output_file, ll_optimize_file)
    optimzer.optimize()
    optimzer.writer()
