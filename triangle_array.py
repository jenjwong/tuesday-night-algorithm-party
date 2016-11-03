import numpy as np
from time import time
from collections import defaultdict

def print_level(triang, lev):
    for row in range(6-lev+1):
        for col in range(row+1):
            print  triang[(row,col,lev)],
        print 

def test_triangle():
    test_triang = [15, -14, -7, 20, -13, -5, -3, 8, 23, -26, 1, -4, -5, -18, 5, -16, 31, 2, 9, 28, 3]
    triang = {}
    rows = 6
    row, col = 0,0
    for k in test_triang:
        triang[(row,col,1)] = k
        triang[(row,col,0)] = 0
        col += 1
        if col > row:
            row += 1
            col = 0
    for k in range(rows+1):
        triang[(rows,k,0)] = 0
            
    print_level(triang, 1)

def numpy_run():
    t0 = time()
    rows = 1000
    t, row, col = 0, 0, 0
    Triang = np.zeros([rows, rows])
    for k in range(rows*(rows+1)/2):
        t = (615949*t + 797807)%2**20
        Triang[row, col] = t - 2**19
        col += 1
        if col > row:
            row += 1
            col = 0
    
    Triang1 = np.zeros([rows, rows])
    Triang2 = np.zeros([rows, rows])
    temp = np.zeros([rows, rows])
    min_init = np.min(Triang)

    for n in range(2,rows):
        print n
        for row in range(rows-n):
            Triang1[row, :row+1] = Triang[row, :row+1] + \
                                   Triang2[row+1, :row+1] + \
                                   Triang2[row+1, 1:row+2] - \
                                   Triang1[row+2, 1:row+2]
        row_min = np.min(Triang1)
        if min_init > row_min:
            min_init = row_min 
        temp = Triang1
        Triang1 = Triang2
        Triang2 = temp
    print 'min sum = ', min_init
    print 'total run time = ', time() - t0
    
def dict_run():
    t0 = time()
    rows = 1000
    t, row, col = 0, 0, 0
    Triang = defaultdict(lambda: 0) 
    for k in range(rows*(rows+1)/2):
        t = (615949*t + 797807)%2**20
        Triang[(row, col)] = t - 2**19
        col += 1
        if col > row:
            row += 1
            col = 0

    Triang1 = defaultdict(lambda: 0) 
    Triang2 = defaultdict(lambda: 0) 
    temp = defaultdict(lambda: 0)     
    min_init = min(Triang.values())

    for n in range(2,rows):
        print n
        for row in range(rows-n):
            for col in range(row+1):
                Triang1[(row, col)] = Triang[(row, col)] + \
                                        Triang2[(row+1, col)] + \
                                        Triang2[(row+1, col+1)] - \
                                        Triang1[(row+2, col+1)]
        row_min = min(Triang1.values())
        if min_init > row_min:
            min_init = row_min 
        temp = Triang1
        Triang1 = Triang2
        Triang2 = temp
    print 'min sum = ', min_init
    print 'total run time = ', time() - t0

def list_run():
    t0 = time()
    rows = 1000
    t, row, col = 0, 0, 0
    Triang = [[0]*rows for x in range(rows)]
    for k in range(rows*(rows+1)/2):
        t = (615949*t + 797807)%2**20
        Triang[row][col] = t - 2**19
        col += 1
        if col > row:
            row += 1
            col = 0
    
    Triang1 = [[0]*rows for x in range(rows)]
    Triang2 = [[0]*rows for x in range(rows)]
    temp = [[0]*rows for x in range(rows)]
    min_init = 17

    for n in range(2,rows):
        print n
        for row in range(rows-n):
            for col in range(row+1):
                Triang1[row][col]  = Triang[row][col]  + \
                                     Triang2[row+1][col]  + \
                                     Triang2[row+1][col+1]  - \
                                     Triang1[row+2][col+1] 
            row_min = min(Triang1[row])
            if min_init > row_min:
                min_init = row_min 
        temp = Triang1
        Triang1 = Triang2
        Triang2 = temp
    print 'min sum = ', min_init
    print 'total run time = ', time() - t0
    
def list_comprehension_run():
    t0 = time()
    rows = 1000
    t, row, col = 0, 0, 0
    Triang = [[0]*rows for x in range(rows)]
    for k in range(rows*(rows+1)/2):
        t = (615949*t + 797807)%2**20
        Triang[row][col] = t - 2**19
        col += 1
        if col > row:
            row += 1
            col = 0
    
    Triang1 = [[0]*rows for x in range(rows)]
    Triang2 = [[0]*rows for x in range(rows)]
    temp = [[0]*rows for x in range(rows)]
    min_init = 17

    for n in range(2,rows):
        print n
        for row in range(rows-n):
            Triang1[row]  = [Triang[row][x]  + \
                            Triang2[row+1][x]  + \
                            Triang2[row+1][x+1]  - \
                            Triang1[row+2][x+1] for x in range(row+1)] 
            row_min = min(Triang1[row])
            if min_init > row_min:
                min_init = row_min 
        temp = Triang1
        Triang1 = Triang2
        Triang2 = temp
    print 'min sum = ', min_init
    print 'total run time = ', time() - t0

if __name__ == "__main__":
    # test_triangle()
    # numpy_run()
    # dict_run()
    # list_run()
    list_comprehension_run()