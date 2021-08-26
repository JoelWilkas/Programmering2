x = int(input())

antal = []

while x > 0:
    antal.append(x)
    x = x-1

pog = []

for i in antal:
    i = int(input("bruh: "))
    pog.append(i)

for i in pog:
    if i % 2 == 0:
        print("Even")
    else:
        print("odd")
