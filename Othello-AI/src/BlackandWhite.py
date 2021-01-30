import numpy as np
import random
import time

X_COORDINATE=0
Y_COORDINATE=1
COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(123)
conor=[(0,0),(0,7),(7,0),(7,7)]
star=[(0,1),(1,0),(1,1),
      (1,7),(0,6),(1,6),
      (6,0),(7,1),(6,1),
      (6,7),(7,6),(6,6)]
direction = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
tempboard=np.zeros((8,8))
 #don't change the class name
def flip(self, move, side, chessboard):
    currentX = move[0]
    currentY = move[1]
    currentSide = side
    opponentSide = -side
    trueFlip = []
    possibleFlip = []
    for i in range(8):
        # 关于反转棋子的数据表示，之后考虑用nparray实现，不知道性能会不会提升
        flag = 0
        stride = 1
        nextPositionX = (currentX + stride * direction[i][0])
        nextPositionY = (currentY + stride * direction[i][1])
        while (0 <= nextPositionX < self.chessboard_size and (
                0 <= nextPositionY < self.chessboard_size)):
            if (chessboard[nextPositionX][nextPositionY] == COLOR_NONE):
                break
            elif (chessboard[nextPositionX][nextPositionY] == opponentSide):
                flag = 1
                stride += 1
                possibleFlip.append((nextPositionX, nextPositionY))
                nextPositionX = (currentX + stride * direction[i][0])
                nextPositionY = (currentY + stride * direction[i][1])
                continue
            elif (chessboard[nextPositionX][nextPositionY] == currentSide):
                if (flag == 1):
                    trueFlip.extend(possibleFlip)
                    possibleFlip.clear()
                    break
                else:
                    possibleFlip.clear()
                    break
    for element in trueFlip:
        chessboard[element[0]][element[1]] = -chessboard[element[0]][element[1]]
class AI(object):


 #chessboard_size, color, time_out passed from agent

    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        self.color = color
        self.candidate_list = []
    def moveOnBoard(self,move,side,chessboard):
        #TODO 可能要做个检查，但现在懒得做
        chessboard[move[0]][move[1]]=side
       # print(chessboard)
        self.flip(move,side,chessboard)
      #  print(chessboard)

    def getMoves(self,chessboard,side)->list:
        empty = np.where(chessboard == COLOR_NONE)  #empty就是棋盘山没有子的
        empty = list((zip(empty[0], empty[1])))     #封装成二维坐标的list
        currentSide = side                         #当前我方side
        opponentSide = -side                       #当前地方side
        candidate_list=[]                          #可能的候选位置

        for possiblePosition in empty:
            currentX = possiblePosition[X_COORDINATE]
            currentY = possiblePosition[Y_COORDINATE]
            for i in range(8):  #八个方向进行搜索
                flag = 0       #一个在某方向上是否搜到元素的flag
                stride = 1
                currentPositionX = (currentX + stride * direction[i][X_COORDINATE]) #当前搜到的x位置，
                currentPositionY = (currentY + stride * direction[i][Y_COORDINATE]) #当前搜到的y位置
                while (0 <= currentPositionX < self.chessboard_size and (          #应该恒定为8
                        0 <= currentPositionY < self.chessboard_size)
                ):
                    if (chessboard[currentPositionX][currentPositionY] == COLOR_NONE): #这个方向不可能翻棋子
                        break
                    elif (chessboard[currentPositionX][currentPositionY]==opponentSide):
                        flag = 1
                        stride += 1
                        currentPositionX = (currentX + stride * direction[i][0])
                        currentPositionY = (currentY + stride * direction[i][1])
                        continue
                    elif (chessboard[currentPositionX][currentPositionY] == currentSide):#这个方向是我方棋子，那么看看之前有没有越过敌方棋子
                        if (flag == 1):
                                candidate_list.append((currentX, currentY))
                                break
                        else:
                            break
                    else:
                        # error
                        break
        return candidate_list

    def flip(self, move, side,chessboard):
        currentX=move[0]
        currentY=move[1]
        currentSide = side
        opponentSide = -side
        trueFlip = []
        possibleFlip = []
        for i in range(8):
            #关于反转棋子的数据表示，之后考虑用nparray实现，不知道性能会不会提升
            flag=0
            stride=1
            nextPositionX=(currentX+stride*direction[i][0])
            nextPositionY = (currentY + stride * direction[i][1])
            while (0 <= nextPositionX < self.chessboard_size and (
                    0 <= nextPositionY < self.chessboard_size)):
                if(chessboard[nextPositionX][nextPositionY]==COLOR_NONE):
                    break
                elif(chessboard[nextPositionX][nextPositionY]==opponentSide):
                    flag=1
                    stride+=1
                    possibleFlip.append((nextPositionX,nextPositionY))
                    nextPositionX = (currentX + stride * direction[i][0])
                    nextPositionY = (currentY + stride * direction[i][1])
                    continue
                elif(chessboard[nextPositionX][nextPositionY]==currentSide):
                    if(flag==1):
                        trueFlip.extend(possibleFlip)
                        possibleFlip.clear()
                        break
                    else:
                        possibleFlip.clear()
                        break
        for element in trueFlip:
            chessboard[element[0]][element[1]] = -chessboard[element[0]][element[1]]
    #排序函数有点不会写，先这样
    def sortmoves(self,move):
        vitualboard=np.copy(tempboard)
        self.moveOnBoard(move,self.color,vitualboard)
        opponentMove=self.getMoves(vitualboard,-self.color).__len__()
        return opponentMove
    def go(self, chessboard):
            global tempboard
            tempboard=np.copy(chessboard)
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
                self.candidate_list=sorted(self.candidate_list,key=self.sortmoves,reverse=True)
                # for e in self.candidate_list:
                #     print((e,self.sortmoves(e)))
                mychoice = self.candidate_list[self.candidate_list.__len__()-1]
                self.candidate_list.extend(lowPriority)
                self.candidate_list.append(mychoice)
            elif (self.candidate_list.__len__() == 0 and lowPriority.__len__()>0):
                self.candidate_list=lowPriority.copy()
                # randomChoice = random.randint(0, self.candidate_list.__len__() - 1)
                # mychoice = self.candidate_list[randomChoice]
                # self.candidate_list.append(mychoice)
            return self.candidate_list
    def endminmax(self,board,currentSide)->(int,int):

        return (0,0)


class state:
    def __init__(self, chessboard,side,steps,chessboard_size):
        self.chessboard=chessboard
        self.side=side
        self.steps=steps
        self.chessboard_size=chessboard_size
    def updateState(self,move):
        pass


    def getScore(self)->(int,int):#先黑后白
        blackScore=sum(self.chessboard==COLOR_BLACK)
        whiteScore=sum(self.chessboard==COLOR_WHITE)
        print("blackScore:",blackScore,",whiteScore:",whiteScore)
        return (blackScore,whiteScore)

    def getMoves(self)->int:
        empty = np.where(self.chessboard == COLOR_NONE)
        empty = list((zip(empty[0], empty[1])))
        currentSide = self.side
        opponentSide = -self.side
        candidate_list=[]
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
                    if (self.chessboard[currentPositionX][currentPositionY] == COLOR_NONE):
                        break
                    elif (self.chessboard[currentPositionX][currentPositionY] ==opponentSide):
                        flag = 1
                        stride += 1
                        currentPositionX = (currentX + stride * direction[i][0])
                        currentPositionY = (currentY + stride * direction[i][1])
                        continue
                    elif (self.chessboard[currentPositionX][currentPositionY] == currentSide):
                        if (flag == 1):
                                candidate_list.append((currentX, currentY))
                                break
                        else:
                            break
                    else:
                        # error

                        break


        return candidate_list.__len__()

# ai = AI( 8, 1, 60)
# chessboard=np.zeros((8,8))
# chessboard[3][3]=COLOR_BLACK
# chessboard[4][4]=COLOR_BLACK
# chessboard[3][4]=COLOR_BLACK
# chessboard[4][3]=COLOR_BLACK
# chessboard[5][4]=COLOR_BLACK
# chessboard[6][4]=COLOR_WHITE
# chessboard[6][3]=COLOR_BLACK
# print(chessboard)
# ts=ai.go(chessboard)
# print(ts)

