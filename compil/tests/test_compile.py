import pytest
import subprocess
from pathlib import Path
import os
import shutil

TRUE_FILES = Path('compil/tests/fixtures/true_files')
TEST_FILES = Path('compil/tests/fixtures/testing_files')
PROGRAMM_OUTPUT = Path('compil/tests/fixtures/output')


def run_compiler(input_file):
    subprocess.run(["python3", "compil/compiler.py", "-f", f"{input_file}", "-o", PROGRAMM_OUTPUT])


def test_compile_types_print():
    run_compiler(TEST_FILES / 'test_types.txt')
    with open(TRUE_FILES / 'types.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}/programm_output.txt', 'r') as f2:
            assert f1.read() == f2.read()

    shutil.rmtree(PROGRAMM_OUTPUT)


def test_math_operand():
    run_compiler(TEST_FILES / 'test_math.txt')
    with open(TRUE_FILES / 'math.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}/programm_output.txt', 'r') as f2:
            assert f1.read() == f2.read()

    shutil.rmtree(PROGRAMM_OUTPUT)


def test_loop_for():
    run_compiler(TEST_FILES / 'test_loop_for.txt')
    with open(TRUE_FILES / 'loop_for.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}/programm_output.txt', 'r') as f2:
            assert f1.read() == f2.read()

    shutil.rmtree(PROGRAMM_OUTPUT)


def test_loop_while():
    run_compiler(TEST_FILES / 'test_loop_while.txt')
    with open(TRUE_FILES / 'loop_while.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}/programm_output.txt', 'r') as f2:
            assert f1.read() == f2.read()

    shutil.rmtree(PROGRAMM_OUTPUT)


def test_loop_dowhile():
    run_compiler(TEST_FILES / 'test_loop_dowhile.txt')
    with open(TRUE_FILES / 'loop_dowhile.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}/programm_output.txt', 'r') as f2:
            assert f1.read() == f2.read()

    shutil.rmtree(PROGRAMM_OUTPUT)


def test_if_ifelse():
    run_compiler(TEST_FILES / 'test_if_ifelse.txt')
    with open(TRUE_FILES / 'if_ifelse.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}/programm_output.txt', 'r') as f2:
            assert f1.read() == f2.read()

    shutil.rmtree(PROGRAMM_OUTPUT)

