import perlin
import math


def faceNormal(i):
    normal = []

    U = [i[1][0] - i[0][0], i[1][1] - i[0][1], i[1][2] - i[0][2]]
    V = [i[2][0] - i[0][0], i[2][1] - i[0][1], i[2][2] - i[0][2]]

    normal.append(U[1] * V[2] - U[2] * V[1])
    normal.append(U[2] * V[1] - U[1] * V[2])
    normal.append(U[0] * V[1] - U[1] * V[0])


    if normal[1] < 0:
        normal[1] = -normal[1]


    return normal


def gen(x=16, y=16, seed = 256, xchunk=0, ychunk=0, normals=False, amplitude = 1):
    v = []
    file = ""

    #Create a list of vertices and add to file
    for i in range(x):
        for j in range(y):
            #v.append([i,0,j])
            v.append([i,perlin.fractal(5, i + x * xchunk, j + y * ychunk, seed),j])
    
    #Add vertices to file string
    for i in v:
        temp = "v " + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n"
        file += temp
    
    #Add gap between vertices and faces
    #file += "\n"

    #Create a list of faces and add to file string
    faces = []
    faceNorm = {}
    vertexNorm = {}
    verts = []

    for i in v:
        #print(i)
        u = False
        d = False
        l = False
        r = False

        #Check if faces should exist
        if i[0] != 0:
            u = True
        if i[0] != x - 1:
            d = True
        if i[2] !=0:
            l = True
        if i[2] != y - 1:
            r = True

        #Add all possible face to list of faces
        if u == True & l == True:
            if i[1] != 0:
                faces.append([[i[0], perlin.custom(i[0] + x * xchunk, i[2] - 1 + y * ychunk, seed, amplitude), i[2] - 1], i, [i[0] - 1, perlin.custom(i[0] - 1 + x * xchunk, i[2] + y * ychunk, seed, amplitude), i[2]]])
            else:
                faces.append([i, [i[0] - 1, i[1], i[2]], [i[0], i[1], i[2] - 1]])

        if d == True & r == True:
            if i[1] != 0:
                faces.append([i, [i[0] + 1, perlin.custom(i[0] + 1 + x * xchunk, i[2] + y * ychunk, seed, amplitude), i[2]], [i[0], perlin.custom(i[0] + x * xchunk, i[2]+ 1 + y * ychunk, seed, amplitude), i[2] + 1]])
            else:
                faces.append([i, [i[0] + 1, i[1], i[2]], [i[0], i[1], i[2] + 1]])
    
    #Add edge faces (Currently redundant as there are no edges)
    for i in v:
        #print(i)
        #North & South
        if i[1] == 1 and (i[0] == 0 or i[0] == x - 1) and i[2] != (y - 1):
            faces.append([i, [i[0], 0, i[2]], [i[0], 1, i[2]+1]])
        elif i[1] == 0 and (i[0] == 0 or i[0] == x - 1) and i[2] != 0:
            faces.append([i, [i[0], 0, i[2]], [i[0], 0, i[2]-1]])
        #East & West
        if i[1] == 1 and (i[2] == 0 or i[2] == y - 1) and i[0] != (x - 1):
            faces.append([i, [i[0], 0, i[2]], [i[0]+1, 1, i[2]]])
        elif i[1] == 0 and (i[2] == 0 or i[2] == y - 1) and i[0] != 0:
            faces.append([i, [i[0], 0, i[2]], [i[0]-1, 0, i[2]]])
    
    #Calculating normals
    if normals != False:
        for i in faces:
            faceNorm[str(i)] = faceNormal(i)
    
        for i in v:
            vertNorm = [0, 0, 0]
            for k in faceNorm.keys():
                if str(i) in k:
                    temp = faceNorm[k]
                    vertNorm[0] -= temp[0]
                    vertNorm[1] -= temp[1]
                    vertNorm[2] -= temp[2]

            normMag = math.sqrt(vertNorm[0] ** 2 + vertNorm[1] **2 + vertNorm[2] ** 2)
            try:
                vertNorm[0] = -vertNorm[0] / normMag
                vertNorm[1] = -vertNorm[1] / normMag
                vertNorm[2] = -vertNorm[2] / normMag
            except:
                vertNorm[0]=vertNorm[1]=vertNorm[2]=0
        
        vertexNorm[str(i)] = vertNorm

    #Add all vertex normals to a list, and then the document
        for i in faceNorm.keys():
            verts.append(faceNorm[i])
        for i in verts:
            temp = "vn " + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n"
            file += temp
    

    #Adding faces to document
    for i in faces:
        #print(i)
        x = i[0]
        y = i[1]
        z = i[2]

        norm1 = [*faceNorm].index(str(i))

        try:
            vert1 = v.index(i[0]) + 1
            vert2 = v.index(i[1]) + 1
            vert3 = v.index(i[2]) + 1
        except:
            print("Not valid points:", str(x), str(y), str(z))
            break

        if normals == True:
            temp = "f " + str(vert1) + "//" + str(vert1) + " " + str(vert2) + "//" + str(vert2) + " " + str(vert3) + "//" + str(vert3) + "\n"
        else:
            temp = "f " + str(vert1) + " " + str(vert2) +  " " + str(vert3) + "\n"
        file += temp
    
    
    f = open("generationTest2.obj", "w")
    f.write(file)
    f.close()

    return file


def gen(x=16, y=16, seed = 256, octaves = 6, bias = 1.2, normals=False):
    print("Generating noise")
    noise = perlinWIP.perlin()
    noise.noise(x, y, seed, octaves, bias)
    noise.prodImg()
    print("Noise generated")

    file = ""
    vert = []

    print("Generating verts")
    for i in range(x):
        for j in range(y):
            #vert.append([i, 0, j])
            vert.append([i, noise.getVal(i, j), j])
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
            if i[1] != 0: 
                face.append([[i[0], noise.getVal(i[0], i[2] - 1), i[2] - 1], i, [i[0] - 1, noise.getVal(i[0] - 1, i[2]), i[2]]])
            else:
                face.append([i, [i[0] - 1, i[1], i[2]], [i[0], i[1], i[2] - 1]])

        if d == True & r == True:
            if i[1] != 0:
                face.append([i, [i[0] + 1, noise.getVal(i[0] + 1, i[2]), i[2]], [i[0], noise.getVal(i[0], i[2] + 1), i[2] + 1]])
            else:
                face.append([i, [i[0] + 1, i[1], i[2]], [i[0], i[1], i[2] + 1]])
    print("Faces generated")
    for i in face:
        vert1 = vert.index(i[0]) + 1
        vert2 = vert.index(i[1]) + 1
        vert3 = vert.index(i[2]) + 1

        file += "f " + str(vert1) + " " + str(vert2) + " " + str(vert3) + "\n"
    print("Faces inserted")

    
    f = open("generationTest5.obj", "w")
    f.write(file)
    f.close()

    return file

#gen(25, 25, 26)