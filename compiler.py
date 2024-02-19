import old_trans
import main
       


if __name__ == '__main__':
    print("Старт")
    exec(open('main.py').read())
    exec(open('translator.py').read())
    print("Стоп")
