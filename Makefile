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

