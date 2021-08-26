from _typeshed import HasFileno
from sys import dont_write_bytecode, getrecursionlimit, stderr
from types import WrapperDescriptorType


dic = {"Finland": "Helsingfors", "Sveige": "Stockholm", "Danmark": "Legoland"}
dic2 = {"Äpple": "Röd", "Banan": "Gul", "Apelsin": "Orange"}

läggTillLand = input("Vilket land vill du lägga till?: ")
läggTillStad = input("Vad heter huvudstaden i landed?: ")
dic.update({läggTillLand: läggTillStad})
print(dic)
tabort = input("Vad vill du ta bort?: ")

if(tabort in dic):
    dic.pop(tabort)
print(dic)
print(dict(dic, **dic2))