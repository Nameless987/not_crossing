import random

L = [[0, 0]] #liste de positions déjà empruntées

posF = [0, 0]

count = 0

ran = random.randint(0, 3)

length = 100

l = len(L)

while(count <= 4 and l < length):
    if(ran == 0):
        state = True
        for i in range(len(L)):
            if(posF[0]-1 == L[i][0] and posF[1] == L[i][1]):
                state = False
                break
        if(state):
            posF[0] -= 1
            L.append([posF[0], posF[1]])
            l += 1
            ran = random.randint(0, 3)
            count = 0
        else:
            ran += 1
            count += 1


    if(ran == 1):
        state = True
        for i in range(len(L)):
            if(posF[0]+1 == L[i][0] and posF[1] == L[i][1]):
                state = False
                break
        if(state):
            posF[0] += 1
            L.append([posF[0], posF[1]])
            l += 1
            ran = random.randint(0, 3)
            count = 0
        else:
            ran += 1
            count += 1

    if(ran == 2):
        state = True
        for i in range(len(L)):
            if(posF[1]+1 == L[i][1] and posF[0] == L[i][0]):
                state = False
                break
        if(state):
            posF[1] += 1
            L.append([posF[0], posF[1]])
            l += 1
            ran = random.randint(0, 3)
            count = 0
        else:
            ran += 1
            count += 1

    if(ran == 3):
        state = True
        for i in range(len(L)):
            if(posF[1]-1 == L[i][1] and posF[0] == L[i][0]):
                state = False
                break
        if(state):
            posF[1] -= 1
            L.append([posF[0], posF[1]])
            l += 1
            ran = random.randint(0, 3)
            count = 0
        else:
            ran = 0
            count += 1

if(count >= 4):
    print("End of the path because no exit")

else:
    print("End of the path because length reached")

print(L)
