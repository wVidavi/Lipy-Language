class Globals:
    def __init__(self):
        self.globals = {
            "__name__": "-default"
        }
    
    def var(self, n:str, v):
        self.globals[n] = eval(v)
    
    def delvar(self, n):
        del self.globals[n]

import time
import os

def tryvar(gb, blank):
    if blank[0] != "$":
        return blank
    if blank[1:] in gb.globals:
        return gb.globals[blank[1:]]
    else:
        return blank

def run(code:str, vl:Globals):
    if code == "":
        return 0

    npcode = str(code)
    code = code.split()

    if len(code) < 1:
        return 0

    if code[0] in vl.globals:
        tp = type(vl.globals[code[0]])
        if tp == int or tp == float:
            tp = "number"
        elif tp == str or tp == bytes:
            tp = "string"
        else:
            tp = "NoneOrUnknown"
        return f"- variable '{code[0]}' is -{tp}: {vl.globals[code[0]]}"
    elif code[0] == "var":
        try:
            vl.var(code[1], code[2])
            return f"- {code[1]} is {code[2]}"
        except:
            return "- some data was not accepted"
    elif code[0] == "del":
        try:
            vl.delvar(code[1])
            return f"- deleted variable '{code[1]}'"
        except:
            return "- variable does not exist"
    elif code[0] == "show":
        res = ""
        for p in code[1::]:
            res += tryvar(vl, p)
            res += " "
        return res
    elif code[0] == "globals":
        return vl.globals
    elif code[0] == "break" or code[0] == "exit":
        exit()
    elif code[0] == "sleep":
        try:
            time.sleep(float(tryvar(vl, code[1])))
        except:
            return f"- that is not a number. can you gimme one instead of {tryvar(vl, code[1])}?"
    elif code[0] == "clear":
        os.system("cls")
    elif code[0] == "eval":
        code = code[1::]
        res = ""
        for calc in code:
            try:
                res += str(eval(calc))
            except:
                res += calc
            res += " "
        return res
    else:
        if npcode.startswith("'") and npcode.endswith("'"):
            return f"-string {npcode}"
        elif npcode[0] in ('0','1','2','3','4','5','6','7','8','9'):
            return f"-number {npcode}"
        else:
            return 0