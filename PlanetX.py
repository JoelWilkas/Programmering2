yta = []

N = int(input("Rader (Just nu funkar bara 3): "))
M = int(input("Kolumner (Just nu funkar bara 2): "))



for i in range(0, M):
    yta.append([])
    for j in range(0, N):
        yta[i].append([])

yta[0][2] = 6
yta[1][0] = 3

for x in range(0,M):
    for y in range(0, N):
        if(yta[x][y] != []):
            if(len(yta[x]) == y + 1):
                z = 0
                while z != len(yta[x]):
                    z += 1
                    if(yta[x][y - z] == []):
                        yta[x][y - z] = yta[x][len(yta[x]) - z] - 1
            else:
                if(yta[x][y] != []):
                    yta[x][y + 1] = yta[x][y] + 1
                    print(yta[x - 1][y + 1] - yta[x][y + 1])
                    if(yta[x - 1][y + 1] - yta[x][y + 1] != 1 and yta[x][y + 1] - yta[x - 1][y + 1] != 1):
                        yta[x][y + 1] = yta[x][y] - 1
                    


            

for x in range(0, len(yta)):
    print(yta[x])