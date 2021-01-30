import numpy as np
from src import BlackandWhite_noalphabeta

myai = BlackandWhite_noalphabeta.AI(8, 1, 5)

board = np.array([
 [ 0 , 0,  0, -1,  0 , 0,  0,  0],
 [ 0 , 0 , 0,  1 ,-1 , 0 , 0,  0],
 [ 0 , 0,  1,  1, -1 ,-1,  0 , 0],
 [ 0 , 0 , 1 ,-1, -1, -1,  0 , 0],
 [ 0 , 0, -1, -1, -1, -1 ,-1 , 0],
 [ 0 ,-1, -1, -1, -1,  0 , 0 , 0],
 [ 0 , 0 , 0,  1,  0,  0,  0,  0],
 [ 0 , 0,  0,  0,  0,  0,  0 , 0]
])
# empty=np.where(board==BlackandWhite_noalphabeta.COLOR_NONE)
# empty=list((zip(empty[0], empty[1])))
#
# print(myai.findavailable(board,1,empty))



# print(myai.evaluation_pattern(myai.two_to_one_map(board),8,0,17))
# print(myai.evaluation_pattern(myai.two_to_one_map(board),14,0,17))

# print(myai.evaluate(myai.two_to_one_map(board),17,0))
myai.go(board)

suchboard=np.array([
 [ 0 , 0,  -1, -1,  0 , 0,  0,  0],
 [ 0 , 0 , 0,  -1 ,-1 , 0 , 0,  0],
 [ 0 , 0,  1,  1, -1 ,-1,  0 , 0],
 [ 0 , 0 , 1 ,1, -1, -1,  0 , 0],
 [ 0 , 0, -1, -1, 1, -1 ,-1 , 0],
 [ 0 ,-1, -1, -1, -1,  1 , 0 , 0],
 [ 0 , 0 , 0,  1,  0,  0,  0,  0],
 [ 0 , 0,  0,  0,  0,  0,  0 , 0]
])

suchboard2=np.array([
 [ 0 , 0,  -1, -1,  0 , 0,  0,  0],
 [ 0 , 0 , 0,  -1 ,-1 , 0 , 0,  0],
 [ 0 , 0,  1,  1, -1 ,1,  0 , 0],
 [ 0 , 0 , 1 ,1, -1, 1,  0 , 0],
 [ 0 , 0, -1, -1, 1, 1 ,1 , 0],
 [ 0 ,1, 1, 1, 1,  1 , 0 , 0],
 [ 0 , 0 , 0,  1,  0,  0,  0,  0],
 [ 0 , 0,  0,  0,  0,  0,  0 , 0]
])


print("length:",len(myai.getMoves(suchboard,1)),myai.getMoves(suchboard,1))

