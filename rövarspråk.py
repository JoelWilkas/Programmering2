from typing import NewType


text = input("").lower()
nyText = ""

konsonantLista = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m" ]

for i in text:
    if(i in konsonantLista):
        nyText += i + "o" + i
    else:
        nyText += i

print(nyText)