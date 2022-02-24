from random import randint

def generateVertices(xScale, yScale):
    vertices = [] 

    for y in range(yScale):
        for x in range(xScale):
            #Replace 1 with noiseValue to enable noise
            #vertices.append([x, 1, y])
            vertices.append([x, randint(1,3), y])
    
    return vertices

def vertexAbove(vertices, vertex, xScale):
    position = vertices.index(vertex)

    return vertices[position + 1]

def vertexRight(vertices, vertex, xScale):
    position = vertices.index(vertex)

    return vertices[position + xScale]

def generateFaces(vertices, xScale, yScale):
    faces = []

    for i in vertices:
        if i[0] != (xScale - 1) and i[2] != (yScale - 1):
            #Find vertices in face
            above = vertexAbove(vertices, i, xScale)
            aboveRight = vertexRight(vertices, above, xScale)
            right = vertexRight(vertices, i, xScale)

            #Add face
            faces.append([i, above, aboveRight])
            faces.append([i, right, aboveRight])
    
    return faces

def createFile(fileName, vertices, faces):
    file = open(fileName, "w")

    #Add vertices
    for i in vertices:
        file.write("v " + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
    
    #Add faces
    for i in faces:
        vert1 = vertices.index(i[0]) + 1 #+ 1 as obj isn't 0 indexed
        vert2 = vertices.index(i[1]) + 1
        vert3 = vertices.index(i[2]) + 1

        file.write("f " + str(vert1) + " " + str(vert2) + " " + str(vert3) + "\n")
    
    file.close()

def runGen(xScale, yScale, fileName):
    vertices = generateVertices(xScale, yScale)
    faces = generateFaces(vertices, xScale, yScale)
    createFile(fileName, vertices, faces)

runGen(64, 64, "Final/testGen.obj")