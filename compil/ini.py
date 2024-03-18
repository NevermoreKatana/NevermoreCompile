from pathlib import Path

COMPILER_DIR = Path('compil')

STANDART_OUPUT_PATH = Path('output_files')

ast_input_file = COMPILER_DIR / 'input.txt'
ast_output_file = COMPILER_DIR / STANDART_OUPUT_PATH / 'ast.json'
program_output_file = COMPILER_DIR / STANDART_OUPUT_PATH / 'programm_output.txt'
ll_output_file = COMPILER_DIR / STANDART_OUPUT_PATH / 'output.ll'
ll_optimize_file = COMPILER_DIR / STANDART_OUPUT_PATH / 'optimized.ll'
executable_file = COMPILER_DIR / STANDART_OUPUT_PATH / 'output'

descr = 'Компилятор процедурного языка NevermoreCompile'
help_f = 'Путь до исходного файла'
help_a = 'Путь сохранения AST файла'
help_o = 'Путь до выходного файла(вывода программы)'
help_od = 'Путь до выходной директории'