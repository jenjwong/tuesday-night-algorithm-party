from random import choice, randint

class Shape:
    def __init__(self, width):
        self.width = width
        self.origin = (0, 0)

    def __str__(self):
        return str(self.origin) + " " + str(self.width)


class Tablau:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bins = [[' ' for _ in range(width)] for _ in range(height)]

    def __str__(self):
        res = ''
        for row in self.bins:
            res += ''.join(row) + '\n'

        return res

    def prynt(self, c, shape):
        x0, y0 = shape.origin
        for j in range(shape.width):
            for i in range(shape.width):
                self.bins[y0 + i][x0 + j] = c

    def reset(self):
        self.bins = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def computeWastedSpace(self):
        return sum(map(lambda row: len(filter(lambda c: c == ' ', row)),
                       self.bins))




def generateShapes(n, maxSize):
    return [Shape(randint(1, maxSize)) for _ in xrange(n)]

        
def dumbPacking(shapes):
    totalWidth = reduce(lambda acc, s: acc + s.width,
                        shapes, 0)
    #maxHeight = max(shapes, lambda s: s.width).width
    maxHeight = reduce(lambda acc, s: max(acc, s.width),
                       shapes[1:], shapes[0].width)

    tab = Tablau(totalWidth, maxHeight)
    x = 0
    for i, s in enumerate(shapes):
        s.origin = (x, s.origin[1])
        tab.prynt('abcdefghijklmnopqrstuvwxyz'[i], s)
        x += s.width

    return tab


def slightlyLessDumbPacking(shapes):
    shapes = sorted(shapes, cmp=lambda s1, s2: s2.width - s1.width)

    
    #totalWidth = reduce(lambda acc, s: acc + s.width,
    #                    shapes[:len(shapes)/2], 0)
    totalWidth = reduce(lambda acc, s: acc + s.width,
                        shapes, 0)
    breakPoint = findBreakPoint(totalWidth/2, shapes)
    firstHalfWidth = reduce(lambda acc, s: acc + s.width,
                            shapes[:breakPoint], 0)
    secondHalfWidth = reduce(lambda acc, s: acc + s.width,
                             shapes[breakPoint:], 0)
    tab = Tablau(max(firstHalfWidth, secondHalfWidth),
                 shapes[0].width + shapes[breakPoint].width)

    x = 0
    i = 0
    for s in shapes[:breakPoint]:
        s.origin = (x, 0)
        tab.prynt('abcdefghijklmnopqrstuvwxyz'[i], s)
        x += s.width
        i += 1

    x = 0
    heightOffset = shapes[0].width
    for s in shapes[breakPoint:]:
        s.origin = (x, heightOffset)
        tab.prynt('abcdefghijklmnopqrstuvwxyz'[i], s)
        x += s.width
        i += 1

    return tab


def findBreakPoint(threshold, shapes):
    accum = 0
    breakPoint = 0
    while accum < threshold:
        accum += shapes[breakPoint].width
        breakPoint += 1

    return breakPoint - 1
