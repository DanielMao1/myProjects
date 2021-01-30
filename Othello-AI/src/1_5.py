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
        # 鍏充簬鍙嶈浆妫嬪瓙鐨勬暟鎹〃绀猴紝涔嬪悗鑰冭檻鐢╪parray瀹炵幇锛屼笉鐭ラ亾鎬ц兘浼氫笉浼氭彁鍗�
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
        #TODO 鍙兘瑕佸仛涓鏌ワ紝浣嗙幇鍦ㄦ噿寰楀仛
        chessboard[move[0]][move[1]]=side
       # print(chessboard)
        self.flip(move,side,chessboard)
      #  print(chessboard)

    def getMoves(self,chessboard,side)->list:
        empty = np.where(chessboard == COLOR_NONE)  #empty灏辨槸妫嬬洏灞辨病鏈夊瓙鐨�
        empty = list((zip(empty[0], empty[1])))     #灏佽鎴愪簩缁村潗鏍囩殑list
        currentSide = side                         #褰撳墠鎴戞柟side
        opponentSide = -side                       #褰撳墠鍦版柟side
        candidate_list=[]                          #鍙兘鐨勫€欓€変綅缃�

        for possiblePosition in empty:
            currentX = possiblePosition[X_COORDINATE]
            currentY = possiblePosition[Y_COORDINATE]
            for i in range(8):  #鍏釜鏂瑰悜杩涜鎼滅储
                flag = 0       #涓€涓湪鏌愭柟鍚戜笂鏄惁鎼滃埌鍏冪礌鐨刦lag
                stride = 1
                currentPositionX = (currentX + stride * direction[i][X_COORDINATE]) #褰撳墠鎼滃埌鐨剎浣嶇疆锛�
                currentPositionY = (currentY + stride * direction[i][Y_COORDINATE]) #褰撳墠鎼滃埌鐨剏浣嶇疆
                while (0 <= currentPositionX < self.chessboard_size and (          #搴旇鎭掑畾涓�8
                        0 <= currentPositionY < self.chessboard_size)
                ):
                    if (chessboard[currentPositionX][currentPositionY] == COLOR_NONE): #杩欎釜鏂瑰悜涓嶅彲鑳界炕妫嬪瓙
                        break
                    elif (chessboard[currentPositionX][currentPositionY]==opponentSide):
                        flag = 1
                        stride += 1
                        currentPositionX = (currentX + stride * direction[i][0])
                        currentPositionY = (currentY + stride * direction[i][1])
                        continue
                    elif (chessboard[currentPositionX][currentPositionY] == currentSide):#杩欎釜鏂瑰悜鏄垜鏂规瀛愶紝閭ｄ箞鐪嬬湅涔嬪墠鏈夋病鏈夎秺杩囨晫鏂规瀛�
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
            #鍏充簬鍙嶈浆妫嬪瓙鐨勬暟鎹〃绀猴紝涔嬪悗鑰冭檻鐢╪parray瀹炵幇锛屼笉鐭ラ亾鎬ц兘浼氫笉浼氭彁鍗�
            flag=0
            stride=1
            nextPositionX=(currentX+stride*direction[i][X_COORDINATE])
            nextPositionY = (currentY + stride * direction[i][Y_COORDINATE])
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
                        for chess in possibleFlip:
                            chessboard[chess[0]][chess[1]]=currentSide
                        possibleFlip.clear()
                        break
                    else:
                        possibleFlip.clear()
                        break
        # for element in trueFlip:
        #     chessboard[element[0]][element[1]] = -chessboard[element[0]][element[1]]
    #鎺掑簭鍑芥暟鏈夌偣涓嶄細鍐欙紝鍏堣繖鏍�
    def sortmoves(self,move):
        vitualboard=np.copy(tempboard)
        self.moveOnBoard(move,self.color,vitualboard)
        opponentMove=self.getMoves(vitualboard,-self.color).__len__()
        return opponentMove
    def sortmoves2(self,move):
        vitualboard=np.copy(tempboard)
        self.moveOnBoard(move,self.color,vitualboard)
        mysteady=self.steadyChess(vitualboard,self.color)
        return mysteady
    def steadyChess(self, chessboard, side):
        steady = 0
        corner=[(0,0),(0,7),(7,7),(7,0)]
        increase=[(0,1),(1,0),(0,-1),(-1,0)]
        stop = [0, 0, 0, 0]
        for direc in range(4):
            if chessboard[corner[direc][0]][corner[direc][1]] == side:
                stop[direc] = 1
                steady += 1
                for j in range(1, 7):
                    if chessboard[corner[direc][0] + increase[direc][0] * j][corner[direc][1] + increase[direc][1] * j] != side:
                        break
                    else:
                        stop[direc] = j + 1
                        steady += 1
        for direc in range(4):
            if chessboard[corner[direc][0]][corner[direc][1]] == side:
                for j in range(1, 7 - stop[direc - 1]):
                    if chessboard[corner[direc][0] - increase[direc - 1][0] * j][corner[direc][1] - increase[direc - 1][1] * j] != side:
                        break
                    else:
                        steady += 1
        vertical = np.zeros((8, 8), dtype=np.int)
        vertical[:, np.sum(abs(chessboard), axis=0) == 8] = True
        horizental = np.zeros((8, 8), dtype=np.int)
        horizental[np.sum(abs(chessboard), axis=1) == 8, :] = True
        diagonal1 = np.zeros((8, 8), dtype=np.int)
        for direc in range(15):
            diagsum = 0
            if direc <= 7:
                sind1 = direc
                sind2 = 0
                jrange = direc + 1
            else:
                sind1 = 7
                sind2 = direc - 7
                jrange = 15 - direc
            for j in range(jrange):
                diagsum += abs(chessboard[sind1 - j][sind2 + j])
            if diagsum == jrange:
                for k in range(jrange):
                    diagonal1[sind1 - j][sind2 + j] = True
        diagonal2 = np.zeros((8, 8), dtype=np.int)
        for direc in range(15):
            diagsum = 0
            if direc <= 7:
                sind1 = direc
                sind2 = 7
                jrange = direc + 1
            else:
                sind1 = 7
                sind2 = 14 - direc
                jrange = 15 - direc
            for j in range(jrange):
                diagsum += abs(chessboard[sind1 - j][sind2 - j])
            if diagsum == jrange:
                for k in range(jrange):
                    diagonal2[sind1 - j][sind2 - j] = True
        steady = sum(
            sum(np.logical_and(np.logical_and(np.logical_and(vertical, horizental), diagonal1), diagonal2)))
        return steady
    def go(self, chessboard):
            global tempboard
            tempboard=np.copy(chessboard)
            # Clear candidate_list, must do this step

            self.candidate_list.clear()

            empty = np.where(chessboard == COLOR_NONE)
            empty = list((zip(empty[0], empty[1])))

            rest_step=empty.__len__()
            phase=64-rest_step
            myColor = self.color
            opponentColor = -self.color
            if(phase<20):
            # for index in occupied:
            # scanned[index[0]][index[1]]=1
                highPriority = []
                lowPriority = []
                # ==================================================================

                # 椤烘椂閽�
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

            elif(phase<45):
                highPriority = []
                lowPriority = []
                # ==================================================================

                # 椤烘椂閽�
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
                    self.candidate_list = sorted(self.candidate_list, key=self.sortmoves2, reverse=False)
                    # for e in self.candidate_list:
                    #     print((e,self.sortmoves(e)))
                    mychoice = self.candidate_list[self.candidate_list.__len__() - 1]
                    self.candidate_list.extend(lowPriority)
                    self.candidate_list.append(mychoice)
                elif (self.candidate_list.__len__() == 0 and lowPriority.__len__() > 0):
                    self.candidate_list = lowPriority.copy()
                    # randomChoice = random.randint(0, self.candidate_list.__len__() - 1)
                    # mychoice = self.candidate_list[randomChoice]
                    # self.candidate_list.append(mychoice)
                return self.candidate_list

            else:#浣跨敤鏆村姏鎼滅储瀹岀編缁堝眬
                self.candidate_list=self.getMoves(chessboard,myColor)
                if(self.candidate_list.__len__()>0):
                    bestmove=self.endminmax(chessboard,myColor)
                    self.candidate_list.append(bestmove)
                return self.candidate_list
    def findavailable(self,chessboard,myColor,empty):
        # for index in occupied:
        # scanned[index[0]][index[1]]=1
        opponentColor=-myColor
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
                                self.candidate_list.append((currentX, currentY))
                                break
                        else:
                            break
                    else:
                        # error

                        break
        return self.candidate_list




    def endminmax(self,board,currentSide)->(int,int):
        blackmovelist=self.getMoves(board,COLOR_BLACK)
        whitemovelist=self.getMoves(board,COLOR_WHITE)
        mymin=100000
        mymax=-100000
        bestmove=(1,1)
        if(blackmovelist.__len__()==0 and whitemovelist.__len__()==0):
            pass
            # 杩涗笉鏉�...
        else:
            if(currentSide==COLOR_BLACK):
                for move in blackmovelist:
                    copyboard = board.copy()
                    self.moveOnBoard(move,currentSide,copyboard)
                    val=self.minMaxSubSearch(copyboard,-currentSide)
                    if(val>mymax):
                        mymax=val
                        bestmove=move
            else:
                for move in whitemovelist:
                    copyboard = board.copy()
                    self.moveOnBoard(move,currentSide,copyboard)
                    val=self.minMaxSubSearch(copyboard,-currentSide)
                    if(val<mymin):
                        mymin=val
                        bestmove=move
        return bestmove




    def minMaxSubSearch(self,board,currentSide)->int:



        blackmovelist=self.getMoves(board,COLOR_BLACK)
        whitemovelist=self.getMoves(board,COLOR_WHITE)
        if(blackmovelist.__len__()==0 and whitemovelist.__len__()==0):
            (bscore,wscore)=self.getBothScore(board)
            return bscore-wscore #宸€�
        else:
            #鏈夌殑涓�
            copyboard=board.copy()
            if(currentSide==COLOR_BLACK):##榛戞柟锛岃繑鍥瀖ax
                mymax = -10000
                mymin = 10000
                score = 0
                if(blackmovelist.__len__()>0):

                    for nextmove in blackmovelist:
                        x=nextmove[X_COORDINATE]
                        y=nextmove[Y_COORDINATE]
                        self.moveOnBoard((x,y),currentSide,copyboard)
                        score=self.minMaxSubSearch(copyboard,-currentSide)
                        if score>mymax:
                            mymax=score
                    return mymax
                else:
                    return self.minMaxSubSearch(copyboard,-currentSide)
            elif (currentSide == COLOR_WHITE):  ##鐧芥柟锛岃繑鍥瀖in
                mymax = -10000
                mymin = 10000
                score = 0
                if (whitemovelist.__len__() > 0):
                    for nextmove in whitemovelist:
                        x = nextmove[X_COORDINATE]
                        y = nextmove[Y_COORDINATE]
                        self.moveOnBoard((x, y), currentSide, copyboard)
                        score = self.minMaxSubSearch(copyboard, -currentSide)
                        if score<mymin:
                            mymin=score
                    return mymin
                else:
                    return self.minMaxSubSearch(copyboard,-currentSide)

    def getBothScore(self,board)->(int,int):
        blackScore = np.where(board == COLOR_BLACK).__len__()
        whiteScore = np.where(board == COLOR_WHITE).__len__()
        # print("blackScore:",blackScore,",whiteScore:",whiteScore)
        return (blackScore, whiteScore)

