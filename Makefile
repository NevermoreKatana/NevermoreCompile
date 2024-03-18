# install:
# 	python3 -m venv .venv
# 	source .venv/bin/activate
# 	pip install -r requirements.txt
# 	deactivate

gramar:
	antlr4 -Dlanguage=Python3 compil/grammar/nevermorecompiler.g4 -o compil/antlr4_gen/
	antlr4 -Dlanguage=Python3 -visitor compil/grammar/nevermorecompiler.g4 -o compil/antlr4_gen/

to_llvm:
	clang output_files/output.ll -o output_files/output

compile:
	python3 compil/compiler.py -f compil/input.txt

full:
	make compile
	make to_llvm
	./output_files/output

install:
	pip install -r requirements.txt

secretkey:
	python -c 'from django.utils.crypto import get_random_string; print(get_random_string(100))'

docker-build:
	docker-compose up --build

requirements:
	pip freeze > requirements.txt