gramar:
	antlr4 -Dlanguage=Python3 grammar/nevermorecompiler.g4 -o antlr4_gen/
	antlr4 -Dlanguage=Python3 -visitor grammar/nevermorecompiler.g4 -o antlr4_gen/

to_llvm:
	clang output_files/output.ll -o output_files/output

compile:
	python compiler.py -f input.txt

full:
	make compile
	make to_llvm
	./output_files/output

install:
	pip install -r requirements.txt

