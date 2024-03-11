import argparse
from main import ast_creator
from translator import translate_to_llvm
import subprocess


def main():
    parser = argparse.ArgumentParser(description='Компилятор процедурного языка NevermoreCompile')

    parser.add_argument('-f', '--file', type=str, help='Путь до исходного файла')
    parser.add_argument('-a', '--ast', type=str, help='Путь сохранения AST файла')
    parser.add_argument('-o', '--output', type=str, help='Путь до выходного файла(вывода программы)')
    args = parser.parse_args()

    input_file = args.file if args.file else None
    ast_file = args.ast if args.ast else None
    output_file = f'{args.output}.txt' if args.output else 'output_files/programm_output.txt'
    
    print("Старт")
    ast_creator(input_file, ast_file)
    translate_to_llvm()
    
    subprocess.run(["clang", "output_files/output.ll", "-o", "output_files/output"])
    subprocess.run(["clear"])
    print("\033[31mEXECUTABLE\033[0m", "\033[32mOUTPUT\033[0m")
    with open(output_file, 'w') as f:
        result = subprocess.run(["./output_files/output"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False, universal_newlines=True)
        print(result.stdout)
        f.write(result.stdout)
        
        print(f"Вывод сохранён в файл {output_file}")
        
    
    
    
if __name__ == "__main__":
    main()



