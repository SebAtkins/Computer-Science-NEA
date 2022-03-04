class noiseFactory:
    # This is a translation of Ken Perlin's original Perlin Noise algorithm into Python,
    # which has been made into a class for ease of use.
    # Octaves use Hugo Elias' definition of persistence.
    list = []

    p = [None] * 512

    permutation = [151,160,137,91,90,15,
    131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
    190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
    88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
    77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
    102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
    135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
    5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
    223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
    129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
    251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
    49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
    138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]

    def __init__(self):
        for i in range(256):
            self.p[256+i] = self.p[i] = self.permutation[i]
    
    def octaveNoise(self, x, y, z, octaves, persistance):
        total = 0
        frequency = 1
        amplitude = 1

        for i in range(octaves):
            total += self.perlin(x * frequency, y * frequency, z * frequency) * amplitude

            frequency *= 2
            amplitude *= persistance
        
        return total
    
    def perlin(self, x, y, z):
        X = int(x) & 255
        Y = int(y) & 255
        Z = int(z) & 255

        x -= int(x)
        y -= int(y)
        z -= int(z)

        u = self.fade(x)
        v = self.fade(y)
        w = self.fade(z)

        A = self.p[X]+Y
        AA = self.p[A]+Z
        AB = self.p[A+1]+Z

        B = self.p[X+1]+Y
        BA = self.p[B]+Z
        BB = self.p[B+1]+Z
    
        return self.lerp(w, self.lerp(v, self.lerp(u, self.grad(self.p[AA], x, y, z),
                                                      self.grad(self.p[BA], x-1, y, z)),
                                         self.lerp(u, self.grad(self.p[AB], x, y-1, z),
                                                      self.grad(self.p[BB], x-1, y-1, z))),
                            self.lerp(v, self.lerp(u, self.grad(self.p[AA+1], x, y, z-1),
                                                      self.grad(self.p[BA+1], x-1, y, z-1)),
                                         self.lerp(u, self.grad(self.p[AB+1], x, y-1, z-1),
                                                      self.grad(self.p[BB+1], x-1, y-1, z-1))))
    
    def returnList(self):
        return self.list
    
    def fade(self, t): 
        return t ** 3 * (t * (t * 6 - 15) + 10)
    
    def lerp(self, t, a, b):
        return a + t * (b - a)
    
    def grad(self, hash, x, y, z):
        h = hash & 15
        u = x if h<8 else y
        v = y if h<4 else (x if h in (12, 14) else z)
        return (u if (h&1) == 0 else -u) + (v if (h&2) == 0 else -v)

    def makeList(self, x, y, z=1234, smooth=25):
        self.list = []
        for i in range(x):
            for j in range(y):
                self.list.append(self.perlin(i / smooth, j / smooth, z))
    
    def makeOctaveList(self, x, y, z=1234, smooth=25, octave=4, persistance=0.35, xPos = 0, yPos = 0):
        self.list = []
        for i in range(x):
            for j in range(y):
                self.list.append(self.octaveNoise((i + xPos * x) / smooth, (j + yPos * y) / smooth, z, octave, persistance))