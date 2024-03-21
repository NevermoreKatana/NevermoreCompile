# install:
# 	python3 -m venv .venv
# 	source .venv/bin/activate
# 	pip install -r requirements.txt
# 	deactivate

gramar:
	cd compil/grammar && antlr4 -Dlanguage=Python3 nevermorecompiler.g4 -o ../antlr4_gen/ && antlr4 -Dlanguage=Python3 -visitor nevermorecompiler.g4 -o ../antlr4_gen/


to_llvm:
	clang compil/outpit_files/output.ll -o compil/output_files/output

compile:
	python3 compil/compiler.py -f compil/input.txt -o compil/outpit_files

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
start-dev:
	python3 manage.py runserver
