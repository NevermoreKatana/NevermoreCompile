from llvmlite import ir, binding
from compil.mixins import ReadWriteMixin


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


def optimize_ll(ll_output_file: str = None, ll_optimize_file: str = None) -> None:
    optimzer = Optimizer(ll_output_file)
    optimzer.optimize()
    optimzer.ll_writer(ll_optimize_file)
