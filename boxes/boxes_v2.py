# from random import randint, seed
import random

class Shape:
    def __init__(self, width):
        self.width = width
        self.origin = (0, 0)

    def __str__(self):
        return str(self.origin) + " " + str(self.width)

class EmptySpace:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width  = width
        self.height = height
        self.flag = 0   # to denote if it was first choice or not

    def __str__(self):
        return str(self.origin) + " " + str(self.width) + " " + str(self.height)

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
        
    # def transpose(self): 
    #     return zip(*self.bins)

    def computeWastedSpace(self):
        return sum(map(lambda row: len(filter(lambda c: c == ' ', row)),
                       self.bins))
                       
    def computeWastedSpaceChido(self):
        maxWidth = self.width
        maxHeight = self.height
        
        for i,row in enumerate(self.bins):
            if sum(x != ' ' for x in self.bins[i]) == 0:              
                maxHeight = i
                break
        self.bins = zip(*self.bins)
        for i,row in enumerate(self.bins):
            if sum(x != ' ' for x in self.bins[i]) == 0:              
                maxWidth = i        
                break
        areaTotal = maxHeight*maxWidth
        occupied_area = sum(map(lambda row: len(filter(lambda c: c != ' ', row)),
                       self.bins))
        print 'width = ', maxWidth, ', height = ',maxHeight, ', min box = ', areaTotal, ', occupied area = ', occupied_area
        print 'wasted space = ', areaTotal - occupied_area 
        # return maxHeight, maxWidth, areaTotal, occupied_area

def generateShapes(n, maxSize, seed = 42):
    random.seed(seed)
    return [Shape(random.randint(1, maxSize)) for _ in xrange(n)]

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

def marginallyLessDumbPacking(shapes):
    shapes = sorted(shapes, cmp=lambda s1, s2: s2.width - s1.width)
    totalWidth = reduce(lambda acc, s: acc + s.width,
                        shapes, 0)
    tab = Tablau(totalWidth, totalWidth)

    emptySpaces = [EmptySpace((0,0), tab.width, tab.height)]
    for i,s in enumerate(shapes):
        bestSpace = findBestSpace(s, emptySpaces, fitThreshold = tab.width)
        s.origin = bestSpace.origin
        new_empty_spaces = insertBox(s, bestSpace)
        emptySpaces.remove(bestSpace)
        emptySpaces.extend(new_empty_spaces)

        tab.prynt('abcdefghijklmnopqrstuvwxyz'[i], s)
    return tab
    
def findBestSpace(shape, emptySpaces, fitThreshold = 1000):
    selection = None
    for es in emptySpaces:
        fit = min(es.width - shape.width, es.height - shape.width)
        if fit >= 0 and fit < fitThreshold:
            selection = es
            fitThreshold = fit
    return selection    

def insertBox(shape, emptySpace):
    originBot = (emptySpace.origin[0] + shape.width, emptySpace.origin[1])
    originTop = (emptySpace.origin[0], shape.width + emptySpace.origin[1])
    widthBot = emptySpace.width - shape.width
    widthTop0 = shape.width
    widthTop1 = emptySpace.width
    heightBot0 = emptySpace.height
    heightBot1 = shape.width
    heightTop = emptySpace.height - shape.width
    if widthBot == 0:
        emptySpaceTop = EmptySpace(originTop, widthTop1, heightTop)
        return [emptySpaceTop]
    if heightTop == 0:
        emptySpaceBot = EmptySpace(originBot, widthBot, heightBot1)
        return [emptySpaceBot]
    if widthBot == 0 and heightTop == 0:
        return []
    # print 's', shape
    # print 'bot', (widthBot, heightBot0), (widthBot, heightBot1)
    # print 'top', (widthTop0, heightTop), (widthTop1, heightTop)
    eccBot0 = max(widthBot, heightBot0)/min(widthBot, heightBot0)
    eccBot1 = max(widthBot, heightBot1)/min(widthBot, heightBot1)
    eccTop0 = max(widthTop0,  heightTop)/min(widthTop0,  heightTop)
    eccTop1 = max(widthTop1,  heightTop)/min(widthTop1,  heightTop)
    if (eccBot0 + eccTop0) <= (eccBot1 + eccTop1):
        emptySpaceBot = EmptySpace(originBot, widthBot, heightBot0)
        emptySpaceTop = EmptySpace(originTop, widthTop0, heightTop)
    else:
        emptySpaceBot = EmptySpace(originBot, widthBot, heightBot1)
        emptySpaceTop = EmptySpace(originTop, widthTop1, heightTop)
    return emptySpaceBot, emptySpaceTop

def findBreakPoint(threshold, shapes):
    accum = 0
    breakPoint = 0
    while accum < threshold:
        accum += shapes[breakPoint].width
        breakPoint += 1

    return breakPoint - 1

if __name__ == "__main__":
    
    # basic parameters
    seed = random.randint(1,1000)
    numBoxes = 10
    maxBoxSize = 10
    
    # initialize tablau, shapes
    tab = Tablau(5,10)
    shapes = generateShapes(numBoxes, maxBoxSize, seed)
    
    # run algo
    tab = marginallyLessDumbPacking(shapes)
    tab.bins = zip(*tab.bins)
    for row in tab.bins:
        print ''.join(row)
        if sum(x != ' ' for x in row) == 0:
            break    
    print 'marginally better algo'
    tab.computeWastedSpaceChido()
            
    # compare to other algos 
    sh = generateShapes(numBoxes, maxBoxSize, seed)
    tab = slightlyLessDumbPacking(sh)
    sh2 = generateShapes(numBoxes, maxBoxSize, seed)
    tab2 = dumbPacking(sh2)
    print 'double packing algo'
    print tab
    tab.computeWastedSpaceChido()
    print 'dumb packing algo'
    print tab2
    tab2.computeWastedSpaceChido()


