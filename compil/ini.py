from pathlib import Path

BASE_DIR = Path('compil/output_files')

input_code = 'input.txt'
ast_output_file = 'ast.json'
program_output_file = 'programm_output.txt'
ll_output_file = 'output.ll'
ll_optimize_file = 'optimized.ll'
executable_file = 'output'

descr = 'Компилятор процедурного языка NevermoreCompile'
help_f = 'Путь до исходного файла'
help_o = 'Путь до выходной директории(вывода программы)'
