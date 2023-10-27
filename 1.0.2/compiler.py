import interpreter as i
import runner as r
import os
import time

g = r.Globals()

os.system("cls")
f = input("File: ")

if not f.endswith(".lp"):
    print("That is not a Lipy file! Lipy files must end with .lp")
    input()
    exit()

with open(f) as source:
    code = source.readlines()

os.system("cls")
for c in range(1,10):
    print("Pls wait...")
    print("["+"#"*c+"]")
    time.sleep(0.2)
    os.system("cls")
print("Completing...")
print("["+"#"*10+"]")
time.sleep(1)
os.system("cls")

for l in code:
    i.do(l, g)