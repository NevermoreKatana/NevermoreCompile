from pathlib import Path

STANDART_OUPUT_PATH = Path('output_files')

ast_input_file = 'input.txt'
ast_output_file = STANDART_OUPUT_PATH / 'ast.json'
program_output_file = STANDART_OUPUT_PATH / 'programm_output.txt'
ll_output_file = STANDART_OUPUT_PATH / 'output.ll'

descr = 'Компилятор процедурного языка NevermoreCompile'
help_f = 'Путь до исходного файла'
help_a = 'Путь сохранения AST файла'
help_o = 'Путь до выходного файла(вывода программы)'
help_od = 'Путь до выходной директории'