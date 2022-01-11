import math
import readImg as read

def makeImg(scale, file, seed, octaves, bias, smooth = 25, xchunk = 0, ychunk = 0):
    read.prodImg(scale, file, seed, octaves, bias, smooth, xchunk, ychunk)

def faceNormal(i):
    normal = []

    U = [i[1][0] - i[0][0], i[1][1] - i[0][1], i[1][2] - i[0][2]]
    V = [i[2][0] - i[0][0], i[2][1] - i[0][1], i[2][2] - i[0][2]]

    normal.append(U[1] * V[2] - U[2] * V[1])
    normal.append(U[2] * V[1] - U[1] * V[2])
    normal.append(U[0] * V[1] - U[1] * V[0])

    if normal[1] < 0:
        normal[0] = - normal[0]
        normal[1] = - normal[1]
        normal[2] = - normal[2]

    return normal

def normVect(list):
    for i in list:
        total = 0

        for j in i:
            total += j ** 2

        total = math.sqrt(total)

        for j in i:
            try:
                j = j / total
            except:
                j = 0

    return list

def genNorms(vert, face):
    vertNorm = []
    for x in range(len(vert)):
        vertNorm.append([0, 0, 0])
    for x in face:
        temp = faceNormal(x)
        for i in x:
            vertNorm[vert.index(i)][0] += temp[0]
            vertNorm[vert.index(i)][1] += temp[1]
            vertNorm[vert.index(i)][2] += temp[2]

    return vertNorm


def imgGen(x=16, y=16, img="swag.png", normals="True", output="output"):
    file = ""
    vert = []

    print("Generating verts")
    for i in range(x):
        for j in range(y):
            vert.append([i,read.getVal(i, j, img), j])
    print("Verts generated")
    for i in vert:
        file += "v " + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n"
    print("Verts inserted")

    print("Generating faces")
    face = []
    for i in vert:
        #Check that vert is not on an edge
        u = False
        d = False
        l = False
        r = False

        if i[0] != 0:
            u = True
        if i[0] != x - 1:
            d = True
        if i[2] !=0:
            l = True
        if i[2] != y - 1:
            r = True

        #Create faces according to edges
        if u == True & l == True: 
            face.append([[i[0], read.getVal(i[0], i[2] - 1, img), i[2] - 1], i, [i[0] - 1, read.getVal(i[0] - 1, i[2], img), i[2]]])

        if d == True & r == True:
            face.append([i, [i[0] + 1, read.getVal(i[0] + 1, i[2], img), i[2]], [i[0], read.getVal(i[0], i[2] + 1, img), i[2] + 1]])
    print("Faces generated")

    
    #Generate normals if selected
    if bool(normals) == True:
        print("Generating normals")
        vertNorms = genNorms(vert, face)
        print("Normals generated")

        print("Normalising normals")
        vertNorms = normVect(vertNorms)
        print("Normals normalised")

        for i in vertNorms:
            file += "vn " + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n"
        print("Normals inserted")
    

    
    #Insert faces
    for i in face:
        vert1 = vert.index(i[0]) + 1
        vert2 = vert.index(i[1]) + 1
        vert3 = vert.index(i[2]) + 1

        if bool(normals) == False:
            file += "f " + str(vert1) + " " + str(vert2) + " " + str(vert3) + "\n"
        else:
            file += "f " + str(vert1) + "//" + str(vert1) + " " + str(vert2) + "//" + str(vert2) + " " + str(vert3) + "//" + str(vert3) + "\n"
    print("Faces inserted")

    f = open(output + ".obj", "w")
    f.write(file)
    f.close()

    return file
