import numpy as np
import random

X_COORDINATE = 0
Y_COORDINATE = 1

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(123)
staticMap = np.array([[500, -25, 10, 5, 5, 10, -25, 500],
                      [-25, -45, 1, 1, 1, 1, -45, -25],
                      [10, 1, 3, 2, 2, 3, 1, 10],
                      [5, 1, 2, 1, 1, 2, 1, 5],
                      [5, 1, 2, 1, 1, 2, 1, 5],
                      [10, 1, 3, 2, 2, 3, 1, 10],
                      [-25, -45, 1, 1, 1, 1, -45, -25],
                      [500, -25, 10, 5, 5, 10, -25, 500]])
conor = [(0, 0), (0, 7), (7, 0), (7, 7)]
star = [(0, 1), (1, 0), (1, 1),
        (1, 7), (0, 6), (1, 6),
        (6, 0), (7, 1), (6, 1),
        (6, 7), (7, 6), (6, 6)]
direction = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
tempboard = np.zeros((8, 8))
default_alpha = -100000000
default_beta = 100000000


# don't change the class name

class AI(object):

    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        self.color = color
        self.candidate_list = []

    def moveOnBoard(self, move, side, chessboard):
        chessboard[move[0]][move[1]] = side
        self.flip(move, side, chessboard)

    #  print(chessboard)

    def steadyChess(self, chessboard, side):
        steady = 0
        corner = [(0, 0), (0, 7), (7, 7), (7, 0)]
        increase = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stop = [0, 0, 0, 0]
        for direc in range(4):
            if chessboard[corner[direc][0]][corner[direc][1]] == side:
                stop[direc] = 1
                steady += 1
                for j in range(1, 7):
                    if chessboard[corner[direc][0] + increase[direc][0] * j][
                        corner[direc][1] + increase[direc][1] * j] != side:
                        break
                    else:
                        stop[direc] = j + 1
                        steady += 1
        for direc in range(4):
            if chessboard[corner[direc][0]][corner[direc][1]] == side:
                for j in range(1, 7 - stop[direc - 1]):
                    if chessboard[corner[direc][0] - increase[direc - 1][0] * j][
                        corner[direc][1] - increase[direc - 1][1] * j] != side:
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

    def getMoves(self, chessboard, side) -> list:
        empty = np.where(chessboard == COLOR_NONE)  # empty就是棋盘山没有子的
        empty = list((zip(empty[0], empty[1])))  # 封装成二维坐标的list
        currentSide = side  # 当前我方side
        opponentSide = -side  # 当前地方side
        candidate_list = []  # 可能的候选位置

        for possiblePosition in empty:
            currentX = possiblePosition[X_COORDINATE]
            currentY = possiblePosition[Y_COORDINATE]
            for i in range(8):  # 八个方向进行搜索
                flag = 0  # 一个在某方向上是否搜到元素的flag
                stride = 1
                currentPositionX = (currentX + stride * direction[i][X_COORDINATE])  # 当前搜到的x位置，
                currentPositionY = (currentY + stride * direction[i][Y_COORDINATE])  # 当前搜到的y位置
                while (0 <= currentPositionX < self.chessboard_size and (  # 应该恒定为8
                        0 <= currentPositionY < self.chessboard_size)
                ):
                    if (chessboard[currentPositionX][currentPositionY] == COLOR_NONE):  # 这个方向不可能翻棋子
                        break
                    elif (chessboard[currentPositionX][currentPositionY] == opponentSide):
                        flag = 1
                        stride += 1
                        currentPositionX = (currentX + stride * direction[i][0])
                        currentPositionY = (currentY + stride * direction[i][1])
                        continue
                    elif (chessboard[currentPositionX][currentPositionY] == currentSide):  # 这个方向是我方棋子，那么看看之前有没有越过敌方棋子
                        if (flag == 1):
                            candidate_list.append((currentX, currentY))
                            break
                        else:
                            break
                    else:
                        # error
                        break

        return candidate_list

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
            nextPositionX = (currentX + stride * direction[i][X_COORDINATE])
            nextPositionY = (currentY + stride * direction[i][Y_COORDINATE])
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
                        for chess in possibleFlip:
                            chessboard[chess[0]][chess[1]] = currentSide
                        possibleFlip.clear()
                        break
                    else:
                        possibleFlip.clear()
                        break
        # for element in trueFlip:
        #     chessboard[element[0]][element[1]] = -chessboard[element[0]][element[1]]

    # 排序函数有点不会写，先这样
    def sortmoves(self, move):
        vitualboard = np.copy(tempboard)
        self.moveOnBoard(move, self.color, vitualboard)
        opponentMove = self.getMoves(vitualboard, -self.color).__len__()
        return opponentMove

    def go(self, chessboard):
        # global tempboard
        # tempboard=np.copy(chessboard)
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        myColor = self.color
        opponentColor = -self.color

        empty = np.where(chessboard == COLOR_NONE)
        empty = list((zip(empty[0], empty[1])))
        rest_step = empty.__len__()
        stage = 64 - rest_step
        available_moves = self.findavailable(chessboard, myColor, empty)  # 这个和candidate_list是一个引用
        if (available_moves.__len__() == 0):
            return self.candidate_list

        if (stage <= 45):
            # randomChoice = random.randint(0, self.candidate_list.__len__() - 1)
            #
            # self.candidate_list.append(randomChoice)
            bestmove = self.rootSearch(self.candidate_list, myColor, chessboard, 2)
            self.candidate_list.append(bestmove)
            return self.candidate_list

        else:  # 使用暴力搜索完美终局
            self.candidate_list = self.getMoves(chessboard, myColor)
            if (self.candidate_list.__len__() > 0):
                bestmove = self.endminmax(chessboard, myColor)
                self.candidate_list.append(bestmove)
            return self.candidate_list

    def rootSearch(self, real_candidate_list, side, chessboard, depth):
        if (real_candidate_list.__len__() > 0):
            bestmove = real_candidate_list[real_candidate_list.__len__() - 1]
            bestscore = -999999
            scores = []
            for move in real_candidate_list:
                flipped = self.makemove(move, side, chessboard)
                score = -self.subsearch(-side, chessboard, depth, default_alpha, default_beta)  # 应该返回一个
                # print("score returned:",score)
                if (score > bestscore):
                    bestscore = score
                    bestmove = move
                self.unmakemove(move, side, chessboard, flipped)
                scores.append(score)
            # print("the score list:",scores,"movelist:",real_candidate_list,"best score:",bestscore,",best move:",(bestmove[0],bestmove[1]))
            return bestmove
        return

    def subsearch(self, side, chessboard, depth, alpha, beta) -> int:
        mymax = -1000000000
        if (depth <= 0):
            if (side == COLOR_BLACK):
                return self.evaluate(chessboard, side)
            else:
                return -self.evaluate(chessboard, side)
        else:
            mylist = self.getMoves(chessboard, side)

            if (mylist.__len__() > 0):
                for valid_move in mylist:
                    flipped = self.makemove(valid_move, side, chessboard)
                    score = -self.subsearch(-side, chessboard, depth - 1, -beta, -alpha)
                    self.unmakemove(valid_move, side, chessboard, flipped)
                    if (score > alpha):
                        alpha = score
                        if (score > beta):  # 剪枝，如果是初始值，score永远不会大于beta
                            return score
                    if (score > mymax):
                        mymax = score
                return mymax
            else:
                opponent_list = self.getMoves(chessboard, -side)
                if (opponent_list.__len__() == 0):
                    (blackscore, whitescore) = self.getBothScore(chessboard)
                    return 1000000 * (blackscore - whitescore)
                else:
                    return -self.subsearch(-side, chessboard, depth, -beta, -alpha)

        pass

    def evaluate(self, board, side):
        if (len(np.where(board == COLOR_BLACK)) == 0):
            return 0
        if (len(np.where(board == COLOR_WHITE)) == 0):
            return 100000
        whilelist = self.getMoves(board, COLOR_WHITE)
        blacklist = self.getMoves(board, COLOR_BLACK)
        return +10 * self.steadyChess(board, COLOR_BLACK) + 15 * (len(blacklist) - len(whilelist))
        # print("random point:",a)

    def makemove(self, move, side, chessboard) -> list:
        chessboard[move[0]][move[1]] = side
        flippedChess = self.flipChess(move, side, chessboard)
        return flippedChess

    def unmakemove(self, move, side, chessboard, flippedchess):
        chessboard[move[0]][move[1]] = COLOR_NONE
        for chess in flippedchess:
            chessboard[chess[0]][chess[1]] = -side
        return

    def flipChess(self, move, side, chessboard):
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

        return trueFlip

    def findavailable(self, chessboard, myColor, empty):
        opponentColor = -myColor
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
                        break
        return self.candidate_list

    def endminmax(self, board, currentSide) -> (int, int):
        blackmovelist = self.getMoves(board, COLOR_BLACK)
        whitemovelist = self.getMoves(board, COLOR_WHITE)
        mymin = 100000
        mymax = -100000
        bestmove = (1, 1)
        if (blackmovelist.__len__() == 0 and whitemovelist.__len__() == 0):
            pass
            # 进不来...
        else:
            if (currentSide == COLOR_BLACK):
                for move in blackmovelist:
                    copyboard = board.copy()
                    self.moveOnBoard(move, currentSide, copyboard)
                    val = self.minMaxSubSearch(copyboard, -currentSide)
                    if (val > mymax):
                        mymax = val
                        bestmove = move
            else:
                for move in whitemovelist:
                    copyboard = board.copy()
                    self.moveOnBoard(move, currentSide, copyboard)
                    val = self.minMaxSubSearch(copyboard, -currentSide)
                    if (val < mymin):
                        mymin = val
                        bestmove = move
        return bestmove

    def minMaxSubSearch(self, board, currentSide) -> int:

        blackmovelist = self.getMoves(board, COLOR_BLACK)
        whitemovelist = self.getMoves(board, COLOR_WHITE)
        if (blackmovelist.__len__() == 0 and whitemovelist.__len__() == 0):
            (bscore, wscore) = self.getBothScore(board)
            return bscore - wscore  # 差值
        else:
            # 有的下
            copyboard = board.copy()
            if (currentSide == COLOR_BLACK):  ##黑方，返回max
                mymax = -10000
                mymin = 10000
                score = 0
                if (blackmovelist.__len__() > 0):

                    for nextmove in blackmovelist:
                        x = nextmove[X_COORDINATE]
                        y = nextmove[Y_COORDINATE]
                        self.moveOnBoard((x, y), currentSide, copyboard)
                        score = self.minMaxSubSearch(copyboard, -currentSide)
                        if score > mymax:
                            mymax = score
                    return mymax
                else:
                    return self.minMaxSubSearch(copyboard, -currentSide)
            elif (currentSide == COLOR_WHITE):  ##白方，返回min
                mymax = -10000
                mymin = 10000
                score = 0
                if (whitemovelist.__len__() > 0):
                    for nextmove in whitemovelist:
                        x = nextmove[X_COORDINATE]
                        y = nextmove[Y_COORDINATE]
                        self.moveOnBoard((x, y), currentSide, copyboard)
                        score = self.minMaxSubSearch(copyboard, -currentSide)
                        if score < mymin:
                            mymin = score
                    return mymin
                else:
                    return self.minMaxSubSearch(copyboard, -currentSide)

    def getBothScore(self, board) -> (int, int):
        blackScore = np.where(board == COLOR_BLACK).__len__()
        whiteScore = np.where(board == COLOR_WHITE).__len__()
        # print("blackScore:",blackScore,",whiteScore:",whiteScore)
        return (blackScore, whiteScore)


class state:
    def __init__(self, chessboard, side, steps, chessboard_size):
        self.chessboard = chessboard
        self.side = side
        self.steps = steps
        self.chessboard_size = chessboard_size

    def updateState(self, move):
        pass

    def getScore(self) -> (int, int):  # 先黑后白
        blackScore = sum(self.chessboard == COLOR_BLACK)
        whiteScore = sum(self.chessboard == COLOR_WHITE)
        # print("blackScore:",blackScore,",whiteScore:",whiteScore)
        return (blackScore, whiteScore)

    def getMoves(self) -> int:
        empty = np.where(self.chessboard == COLOR_NONE)
        empty = list((zip(empty[0], empty[1])))
        currentSide = self.side
        opponentSide = -self.side
        candidate_list = []
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
                    elif (self.chessboard[currentPositionX][currentPositionY] == opponentSide):
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

# ai = AI( 8, -1, 60)
# # chessBoard=np.zeros((10,10))
# chessBoard=np.array([[0,0,0,0,-1,-1,1,-1],
# [0,1,1,-1,-1,1,1,1],
# [1,1,1,-1,1,-1,1,1],
# [-1,-1,-1,1,1,-1,1,1],
# [-1,-1,-1,-1,-1,1,1,1],
# [-1,-1,-1,-1,-1,1,1,1],
# [-1,-1,-1,-1,-1,1,1,0],
# [-1,-1,-1,-1,-1,-1,-1,-1]])
# ts=ai.go(chessBoard)
