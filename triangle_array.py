import numpy as np
from time import time

t0 = time()

# test_triang = [15, -14, -7, 20, -13, -5, -3, 8, 23, -26, 1, -4, -5, -18, 5, -16, 31, 2, 9, 28, 3]
# triang = {}
# rows = 6
# Triang = np.zeros([rows, rows])
# row, col = 0,0
# for k in test_triang:
#     Triang[row,col] = k
#     # triang[(row,col,0)] = 0
#     col += 1
#     if col > row:
#         row += 1
#         col = 0
        
# for row in range(6):
#     for col in range(row+1):
#         print  Triang[row,col],
#     print 

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
min_init = np.min(Triang)

Triang_new = np.zeros([rows+1, rows+1])
for n in range(2,rows):
    print n
    # Triang_new = np.zeros([rows, rows])
    for row in range(rows-n):
        # for col in range(row+1):
        #     Triang_new[row,col] = Triang[row, col] + \
        #                              Triang2[row+1, col] + \
        #                              Triang2[row+1, col+1] - \
        #                              Triang1[row+2, col+1] 
       
        # temp = np.zeros(rows+1)
        temp = Triang[row, :row+1] + \
                                 Triang2[row+1, :row+1] + \
                                 Triang2[row+1, 1:row+2] - \
                                 Triang1[row+2, 1:row+2]
        Triang_new[row, :row+1] = temp
    row_min = np.min(Triang_new)
    if min_init > row_min:
        min_init = row_min 
    Triang1 = Triang2
    Triang2 = Triang_new

print min_init
print time() - t0