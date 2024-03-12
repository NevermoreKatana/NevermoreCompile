import argparse
from ast_create import ast_creator
from translator import translate_to_llvm
import subprocess
from ini import *

def main():
    parser = argparse.ArgumentParser(description=descr)

    parser.add_argument('-f', '--file', type=str, help=help_f)
    parser.add_argument('-a', '--ast', type=str, help=help_a)
    parser.add_argument('-o', '--output', type=str, help=help_o)
    parser.add_argument('-od', '--outputdir', type=str, help=help_od)
    args = parser.parse_args()

    input_file = args.file if args.file else None
    ast_file = args.ast if args.ast else None
    output_file = f'{args.output}.txt' if args.output else program_output_file
    
    subprocess.run(["clear"])
    print("Старт")
    ast_creator(input_file, ast_file)
    translate_to_llvm()
    
    subprocess.run(["clang", STANDART_OUPUT_PATH / "output.ll", "-o", STANDART_OUPUT_PATH / "output"])

    print("\033[31mEXECUTABLE\033[0m", "\033[32mOUTPUT\033[0m")
    with open(output_file, 'w') as f:
        result = subprocess.run(["./output_files/output"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False, universal_newlines=True)
        print(result.stdout)
        f.write(result.stdout)
        
        print(f"Вывод сохранён в файл {output_file}".upper())
        
    
    
    
if __name__ == "__main__":
    main()



