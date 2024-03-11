import pytest
import subprocess
from pathlib import Path
import os


TRUE_FILES = Path('tests/fixtures/true_files')
TEST_FILES = Path('tests/fixtures/testing_files')
PROGRAMM_OUTPUT = Path('tests/fixtures/programm_output')

def run_compiler(input_file):
    subprocess.run(["python3", "compiler.py", "-f", f"{input_file}", "-o", f"{PROGRAMM_OUTPUT}"])

def test_compile_types_print():
    run_compiler(TEST_FILES / 'test_types.txt')
    with open(TRUE_FILES / 'types.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}.txt', 'r') as f2:
            assert f1.read() == f2.read()
            
    os.remove(f'{PROGRAMM_OUTPUT}.txt')

def test_math_operand():
    run_compiler(TEST_FILES / 'test_math.txt')
    with open(TRUE_FILES / 'math.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}.txt', 'r') as f2:
            assert f1.read() == f2.read()
            
    os.remove(f'{PROGRAMM_OUTPUT}.txt')


def test_loop_for():
    run_compiler(TEST_FILES / 'test_loop_for.txt')
    with open(TRUE_FILES / 'loop_for.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}.txt', 'r') as f2:
            assert f1.read() == f2.read()
            
    os.remove(f'{PROGRAMM_OUTPUT}.txt')
    
    
def test_loop_while():
    run_compiler(TEST_FILES / 'test_loop_while.txt')
    with open(TRUE_FILES / 'loop_while.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}.txt', 'r') as f2:
            assert f1.read() == f2.read()
            
    os.remove(f'{PROGRAMM_OUTPUT}.txt')
    
def test_loop_dowhile():
    run_compiler(TEST_FILES / 'test_loop_dowhile.txt')
    with open(TRUE_FILES / 'loop_dowhile.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}.txt', 'r') as f2:
            assert f1.read() == f2.read()
            
    os.remove(f'{PROGRAMM_OUTPUT}.txt')


def test_if_ifelse():
    run_compiler(TEST_FILES / 'test_if_ifelse.txt')
    with open(TRUE_FILES / 'if_ifelse.txt', 'r') as f1:
        with open(f'{PROGRAMM_OUTPUT}.txt', 'r') as f2:
            assert f1.read() == f2.read()
            
    os.remove(f'{PROGRAMM_OUTPUT}.txt')