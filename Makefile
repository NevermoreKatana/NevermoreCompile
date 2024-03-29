gramar:
	cd compil/grammar && antlr4 -Dlanguage=Python3 nevermorecompiler.g4 -o ../antlr4_gen/ && antlr4 -Dlanguage=Python3 -visitor nevermorecompiler.g4 -o ../antlr4_gen/

compile:
	python3 compil/compiler.py -f compil/input.txt -o compil/output_files

install:
	pip install -r requirements.txt

secretkey:
	python -c 'from django.utils.crypto import get_random_string; print(get_random_string(100))'

requirements:
	pip freeze > requirements.txt

start-dev:
	python3 manage.py runserver
