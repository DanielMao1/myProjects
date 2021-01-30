import numpy as np
import random
import time

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(123)
conor = [(0, 0), (0, 7), (7, 0), (7, 7)]
star = [(0, 1), (1, 0), (1, 1),
        (1, 7), (0, 6), (1, 6),
        (6, 0), (7, 1), (6, 1),
        (6, 7), (7, 6), (6, 6)]
direction = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


# don't change the class name

class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        self.color = color
        self.candidate_list = []



    def go(self, chessboard):

        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        empty = np.where(chessboard == COLOR_NONE)
        empty = list((zip(empty[0], empty[1])))
        # for index in occupied:
        # scanned[index[0]][index[1]]=1
        highPriority = []
        lowPriority = []
        # ==================================================================
        myColor = self.color
        opponentColor = -self.color
        # 顺时针
        for possiblePosition in empty:
            currentX = possiblePosition[0]
            currentY = possiblePosition[1]
            for i in range(8):  #
                flag = 0
                stride = 1
                currentPositionX = (currentX + stride * direction[i][0])
                currentPositionY = (currentY + stride * direction[i][1])
                while (0 <= currentPositionX < self.chessboard_size and (
                        0 <= currentPositionY < self.chessboard_size)
                ):
                    if (chessboard[currentPositionX][currentPositionY] == COLOR_NONE):
                        break
                    elif (chessboard[currentPositionX][currentPositionY] == opponentColor):
                        flag = 1
                        stride += 1
                        currentPositionX = (currentX + stride * direction[i][0])
                        currentPositionY = (currentY + stride * direction[i][1])
                        continue
                    elif (chessboard[currentPositionX][currentPositionY] == myColor):
                        if (flag == 1):
                            # if ((currentX, currentY) not in self.candidate_list):
                            if ((currentX, currentY) in conor):
                                highPriority.append((currentX, currentY))
                                break
                            elif ((currentX, currentY) in star):
                                lowPriority.append((currentX, currentY))
                                break
                            else:
                                self.candidate_list.append((currentX, currentY))
                                break
                        else:
                            break
                    else:
                        # error

                        break

        if (highPriority.__len__() > 0):
            self.candidate_list.extend(lowPriority)
            self.candidate_list.extend(highPriority)
        elif (self.candidate_list.__len__() > 0):
            randomChoice = random.randint(0, self.candidate_list.__len__() - 1)
            mychoice = self.candidate_list[randomChoice]
            self.candidate_list.extend(lowPriority)
            self.candidate_list.append(mychoice)
        elif (self.candidate_list.__len__() == 0 and lowPriority.__len__() > 0):
            self.candidate_list = lowPriority.copy()
            # randomChoice = random.randint(0, self.candidate_list.__len__() - 1)
            # mychoice = self.candidate_list[randomChoice]
            # self.candidate_list.append(mychoice)
        return self.candidate_list

    # def checkEachChess(self,myChesses,chessBoard):
    #     opponentColor=-self.color
    #     direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    #     templist=[]
    #     flag = 0
    #     for possiblePosition in myChesses:
    #         currentX=possiblePosition[0]
    #         currentY=possiblePosition[1]
    #         for i in range(8):  # 思路与落子的思路类似，但不同的是这里当搜索到最后的同色棋子时，进行加和操作而非翻面操作
    #             flag=0
    #             stride = 1
    #             currentPositionX=(currentX + stride  * direction[i][0])
    #             currentPositionY=(currentY + stride  * direction[i][1])
    #             while (0 <= currentPositionX< self.chessboard_size and (
    #                     0 <= currentPositionY < self.chessboard_size) and
    #                     (chessBoard[currentPositionX][currentPositionY] == -opponentColor)):
    #
    #                     if (chessBoard[currentPositionX][currentPositionY] ==opponentColor):
    #                         flag =1
    #                         stride+=1
    #                         currentPositionX = (currentX + stride * direction[i][0])
    #                         currentPositionY = (currentY + stride * direction[i][1])
    #                         continue
    #                     elif(chessBoard[currentPositionX][currentPositionY] ==COLOR_NONE):
    #                         if(flag==1):
    #
    #
    #                                 templist.append(zip(currentPositionX,currentPositionY))
    #                     else:
    #                         break
    #     self.list=templist
    #     return templist

    # 左上

    # 上
    # 右上
    # 右
    # 右下
    # 下
    # 左下
    # 左

# The input is current chessboard.


# Write your algorithm here
# Here is the simplest sample:Random decision
# idx = np.where(chessboard == COLOR_NONE)
# idx = list(zip(idx[0], idx[1]))
# ==============Find new pos========================================
# Make sure that the position of your decision in chess board is empty.
# If not, the system will return error.
# Add your decision into candidate_list, Records the chess board
# You need add all the positions which is valid
# candidate_list example: [(3,3),(4,4)]
# You need append your decision at the end of the candidate_list,
# we will choose the last element of the candidate_list as the position you choose
#  # If there is no valid position, you must return a empty list.
ai = AI( 8, -1, 60)
# chessBoard=np.zeros((10,10))
chessBoard=np.array([[0,0,0,0,-1,-1,1,-1],
[0,1,1,-1,-1,1,1,1],
[1,1,1,-1,1,-1,1,1],
[-1,-1,-1,1,1,-1,1,1],
[-1,-1,-1,-1,-1,1,1,1],
[-1,-1,-1,-1,-1,1,1,1],
[-1,-1,-1,-1,-1,1,1,0],
[-1,-1,-1,-1,-1,-1,-1,-1]])
ts=ai.go(chessBoard)

# print('hello')
# print(ts)
# print('world')
