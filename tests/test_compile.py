import pytest
import subprocess
from pathlib import Path



TRUE_FILES = Path('fixtures/true_files')
TEST_FILES = Path('fixtures')


def run_compiler():
    subprocess.run(["/bin/sh", "compile.sh", ">", "fixtures/script_output.txt"])
    subprocess.run(["python3", "output_cleaner.py"])

def test_compile_types():
    subprocess.run(["/bin/sh", "compile.sh", ">", "fixtures/script_output.txt"])
    subprocess.run(["python3", "output_cleaner.py"])
    

run_compiler()