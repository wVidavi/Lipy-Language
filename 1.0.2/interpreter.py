import runner as r
import os
import time

def do(_in_, glo):
    _out_ = r.run(_in_, glo)
    print(_out_)

if __name__ == "__main__":
    os.system("cls")
    g=r.Globals()
    print("Lipy Interpreter 1.0.0")
    while 1:
        do(input(">>> "), g)