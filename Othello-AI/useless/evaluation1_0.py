# import numpy
#
# def getstable(board, color):
#     stable = [0,0,0]
#     # 角, 边, 八个方向都无空格
#     cind1 = [0,0,7,7]
#     cind2 = [0,7,7,0]
#     inc1 = [0,1,0,-1]
#     inc2 = [1,0,-1,0]
#     stop = [0,0,0,0]
#     for i in range(4):
#         if board[cind1[i]][cind2[i]] == color:
#             stop[i] = 1
#             stable[0] += 1
#             for j in range(1,7):
#                 if board[cind1[i]+inc1[i]*j][cind2[i]+inc2[i]*j] != color:
#                     break
#                 else:
#                     stop[i] = j + 1
#                     stable[1] += 1
#     for i in range(4):
#         if board[cind1[i]][cind2[i]] == color:
#             for j in range(1,7-stop[i-1]):
#                 if board[cind1[i]-inc1[i-1]*j][cind2[i]-inc2[i-1]*j] != color:
#                     break
#                 else:
#                     stable[1] += 1
#     diag1full = numpy.zeros((8, 8), dtype=numpy.int)
#     for i in range(15):
#         diagsum = 0
#         if i <= 7:
#             sind1 = i
#             sind2 = 0
#             jrange = i+1
#         else:
#             sind1 = 7
#             sind2 = i-7
#             jrange = 15-i
#         for j in range(jrange):
#             diagsum += abs(board[sind1-j][sind2+j])
#         if diagsum == jrange:
#             for k in range(jrange):
#                 diag1full[sind1-j][sind2+j] = True
#     diag2full = numpy.zeros((8, 8), dtype=numpy.int)
#     for i in range(15):
#         diagsum = 0
#         if i <= 7:
#             sind1 = i
#             sind2 = 7
#             jrange = i+1
#         else:
#             sind1 = 7
#             sind2 = 14-i
#             jrange = 15-i
#         for j in range(jrange):
#             diagsum += abs(board[sind1-j][sind2-j])
#         if diagsum == jrange:
#             for k in range(jrange):
#                 diag2full[sind1-j][sind2-j] = True
#     stable[2] = sum(sum(numpy.logical_and(numpy.logical_and(numpy.logical_and(colfull, rowfull), diag1full), diag2full)))
#     return stable
#
#
# def diagnalstable(board,color):
#     colfull = numpy.zeros((8, 8), dtype=numpy.int)
#     colfull[:,numpy.sum(abs(board), axis = 0) == 8] = True
#     rowfull = numpy.zeros((8, 8), dtype=numpy.int)
#     rowfull[numpy.sum(abs(board), axis = 1) == 8,:] = True
#     diag1full = numpy.zeros((8, 8), dtype=numpy.int)
#     direction1=[(1,1)
#     direction2=(-1,-1)
#
#
#     for i in range(-7,8):
#         diag=board.diagonal(offset=i)
#         print(i,"maxtrix:",diag)
#         print("sum result:",numpy.sum(abs(diag)))
#         if(numpy.sum(abs(diag))==diag.__len__()):
#             for i in range()
#         numpy.fill_diagonal(board,)
#
# arr = numpy.arange(64)
# arr=arr.reshape(8,8)
# print("origin arr:\n",arr)
# diagnalstable(arr,1)
#
# # a=[[1,2,3,4],
# #    [5,6,7,8],
# #    [9,10,11,12]]
# # board=numpy.array(a)
# # board.diagonal()
# #
# colfull = numpy.zeros((8, 8), dtype=numpy.int)
# colfull[:, numpy.sum(abs(board), axis=0) == 8] = True
# rowfull = numpy.zeros((8, 8), dtype=numpy.int)
# rowfull[numpy.sum(abs(board), axis=1) == 8, :] = True
# # diag1full = numpy.zeros((8, 8), dtype=numpy.int)
#
#
