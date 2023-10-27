import runner

def newBank():
    return runner.Globals()

def interpreter(code:str, bank:runner.Globals):
    return runner.run(code, bank)

def help():
    return """First, create your Global bank
Use newBank() and save in a variable.
to run code, just do: interpreter(yourCode, yourBank)
In order to use lipy you need py3.9.9"""