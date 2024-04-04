import argparse
import subprocess
from ast_create import ast_creator
from translator import translate_to_llvm
from optimizer import optimize_ll, ast_optimizer
from ini import *
import os
import sys
import time
import datetime


def main():
    parser = argparse.ArgumentParser(description=descr)

    parser.add_argument('-f', '--file', type=str, help=help_f)
    parser.add_argument('-o', '--output', type=str, help=help_o)
    args = parser.parse_args()

    output_dir = args.output if args.output else BASE_DIR
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not args.file:
        try:
            raise FileNotFoundError(
                "Нужно передать входной файл в аргумент -f, введите -h, чтобы увидеть все доступные аргументы")
        except FileNotFoundError as e:
            print(str(e))
            sys.exit(1)
    if not args.output:
        try:
            raise FileNotFoundError(
                "Нужно передать выходную директорию в аргумент -o, введите -h, чтобы увидеть все доступные аргументы")
        except FileNotFoundError as e:
            print(str(e))
            sys.exit(1)
    input_file = args.file if args.file else input_code
    output_file = os.path.join(output_dir, program_output_file)
    ast_file = os.path.join(output_dir, ast_output_file)
    ll = os.path.join(output_dir, ll_output_file)
    ll_opt = os.path.join(output_dir, ll_optimize_file)
    exec_file = os.path.join(output_dir, executable_file)
    
    subprocess.run(["clear"])
    start_time = time.time()
    print("Старт")
    ast_creator(input_file, ast_file)
    print('Оптимизация AST дерева')
    ast_optimizer(ast_file)
    print('Перевод в машинно-независимый код')
    translate_to_llvm(ast_file, ll)
    print('Оптимизация машинно-независимого кода')
    optimize_ll(ll, ll_opt)

    subprocess.run(["clang", ll_opt, "-o", exec_file])

    print("\033[31mEXECUTABLE\033[0m", "\033[32mOUTPUT\033[0m")
    with open(output_file, 'w') as f:
        result = subprocess.run([f"./{exec_file}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, check=False, universal_newlines=True)
        print(result.stdout)
        f.write(result.stdout)

        print(f"Вывод сохранён в файл {output_file}".upper())
    print(f"Время выполнения {datetime.timedelta(seconds=(time.time() - start_time))}")

if __name__ == "__main__":
    main()
