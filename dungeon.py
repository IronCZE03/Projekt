from random import randint
'''with open("commands.txt", "r") as C:
    c = C.read()'''

dungeon = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append("     ")
    dungeon.append(temp)

dungeon[0][0] = "room"

coords = []
with open("doors.txt", "r") as D:
    d = D.readlines()
    for k in d:
        k = k.split(":")
        k.remove("\n")
        coords.append(k)
        
howMany = randint(0, 11)
s = 0
while s < howMany:
    which = randint(1, 11)
    for i, row in enumerate(coords):
        if i == which:
            coords[i][0] = 0
            s += 1

for i, row in enumerate(coords):
    if coords[i][0] != 0:
        coords[i][0] = 1

for i, rooms in enumerate(dungeon):
    for j, room in enumerate(rooms):
        s = str(i) + ";" + str(j)
        for y, row in enumerate(coords):
            if coords[y][1] == s and coords[y][0] == 1:
                A = coords[y][1].split(';')[:1]
                B = coords[y][1].split(';')[1:]
                C = coords[y][2].split(';')[:1]
                D = coords[y][2].split(';')[1:]
                a = int(A[0])
                b = int(B[0])
                c = int(C[0])
                d = int(D[0])
                for k, rooms in enumerate(dungeon):
                    for l, room in enumerate(rooms):
                        if dungeon[c][d] != "room" and dungeon[a][b] == "room":
                            dungeon[c][d] = "room"
                            continue
 
for rooms in dungeon:
    for room in rooms:
        print(room, end = " ")
    print(end = "\n")
