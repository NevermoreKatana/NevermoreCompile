import argparse
import subprocess
from ast_create import ast_creator
from translator import translate_to_llvm
from optimizer import optimize_ll
from ini import *
import os


def main():
    parser = argparse.ArgumentParser(description=descr)

    parser.add_argument('-f', '--file', type=str, help=help_f)
    parser.add_argument('-o', '--output', type=str, help=help_o)
    args = parser.parse_args()

    output_dir = args.output if args.output else BASE_DIR
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    input_file = args.file if args.file else input_code
    output_file = os.path.join(output_dir,program_output_file)
    ast_file = os.path.join(output_dir, ast_output_file)
    ll = os.path.join(output_dir, ll_output_file)
    ll_opt = os.path.join(output_dir, ll_optimize_file)
    exec_file = os.path.join(output_dir, executable_file)

    subprocess.run(["clear"])
    print("Старт")
    ast_creator(input_file, ast_file)
    print('Перевод в машинно-независимый код')
    translate_to_llvm(ast_file, ll)
    print('Оптимизация машинно-независимого кода')
    optimize_ll(ll, ll_opt)

    subprocess.run(["clang",ll_opt, "-o", exec_file])

    print("\033[31mEXECUTABLE\033[0m", "\033[32mOUTPUT\033[0m")
    with open(output_file, 'w') as f:
        result = subprocess.run([f"./{exec_file}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, check=False, universal_newlines=True)
        print(result.stdout)
        f.write(result.stdout)

        print(f"Вывод сохранён в файл {output_file}".upper())


if __name__ == "__main__":
    main()
