from compil.ast_create import ast_creator
from compil.translator import translate_to_llvm
from compil.optimizer import optimize_ll
import threading
import subprocess
import tempfile
import os


tmp_dir = os.path.join(os.getcwd(), 'tmp_files')
os.makedirs(tmp_dir, exist_ok=True)

def code_to_txt(input_code: str):
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, dir=tmp_dir) as input_txt:
        with open(input_txt.name, 'w') as f:
            f.write(input_code)

    input_txt.close()
    return input_txt

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def online_compile(input_code: str):
    input_file = code_to_txt(input_code)
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False, dir=tmp_dir) as ast_file, \
            tempfile.NamedTemporaryFile(suffix=".ll", delete=False, dir=tmp_dir) as ll_file, \
            tempfile.NamedTemporaryFile(suffix=".ll", delete=False, dir=tmp_dir) as ll_optimize_file, \
            tempfile.NamedTemporaryFile(suffix="", delete=False, dir=tmp_dir) as executable_file:
        ast_creator(input_file, ast_file.name)
        translate_to_llvm(ast_file.name, ll_file.name)
        optimize_ll(ll_file.name, ll_optimize_file.name)

        ast_file.close()
        ll_file.close()
        ll_optimize_file.close()
        executable_file.close()


        subprocess.run(["clang", ll_optimize_file.name, "-o", executable_file.name])

        result = subprocess.run([executable_file.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, check=False, universal_newlines=True)
        for file in [ast_file.name, ll_file.name, ll_optimize_file.name, executable_file.name, input_file.name]:
            timer = threading.Timer(300, delete_file, args=[file])
            timer.start()
        return {"output": result.stdout,
                "ast_file": os.path.basename(ast_file.name),
                "ll_file": os.path.basename(ll_file.name),
                "ll_opt_file": os.path.basename(ll_optimize_file.name),
                "executable_file": os.path.basename(executable_file.name)}

