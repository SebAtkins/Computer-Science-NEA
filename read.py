import objGenerate

def read(inFile):
    lines = []
    linesTest = {}

    f = open(inFile, "r")
    for x in f:
        if x[:2] =="v ":
            temp=x[2:]
            pos=temp.find(" ")
            temp = temp[pos+1:]
            pos2=temp.find(" ")
            temp = float(temp[:pos2])
            if temp == 1.0:
                linesTest[x] = [float(x[2:pos+2]), float(x[x.rfind(" "):])]
                #print(temp)
                #y = x[:pos+1] + " " + str(temp*(randint(1,10)/100)) + " " + x[pos2+pos+4:]
                #print(y)
                #x = y
        lines.append(x)
    f.close()

def readF():
    linesTest = {}

    f = objGenerate.gen(32,32)
    lines = f.split("\n")

    for x in lines:
        if x[:2] =="v ":
            temp=x[2:]
            pos=temp.find(" ")
            temp = temp[pos+1:]
            pos2=temp.find(" ")
            temp = float(temp[:pos2])
            if temp == 1.0:
                linesTest[x] = [float(x[2:pos+2]), float(x[x.rfind(" "):])]

    return lines, linesTest


#read("test.obj")
#readF()