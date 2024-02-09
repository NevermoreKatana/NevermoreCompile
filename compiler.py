import lvm
import main

if __name__ == '__main__':
    print("Старт")
    exec(open('main.py').read())
    exec(open('lvm.py').read())
    print("Стоп")
