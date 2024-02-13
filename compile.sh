source ./env/bin/activate
python compiler.py
clang output_files/output.ll -o output_files/output
#clear
echo -e "\033[32mEXECUTABLE  \033[31mOUTPUT\033[0m"
./output_files/output