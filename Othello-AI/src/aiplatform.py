import time

import numpy as np
from src import BlackAndWhite1_0
# from src import BlackandWhite1_2
from src import BlackAndWhite1_0
# from src import BlackandWhite1_1
# from src import BlackandWhite_noalphabeta
# from src import blackandwhite1_5
from src import BlackAndWhite1_6
from src import blackandwhite1_5_half_test
from src import BlackAndWhite1_6_small
# from src import BlackandWhite_fastinit
from src import current_program
from src import program_current_modify

from src import BlackandWhite1_4

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0

TIME = 0.2

blackmaxtime=0
whitemaxtime=0
blacktime=0
blackstep=0
whitetime=0
whitestep=0

class AIPlatform:

    def __init__(self, chessboard_size):
        player1 = BlackAndWhite1_0.AI(chessboard_size, COLOR_BLACK, TIME)
        player2 = BlackAndWhite1_6.AI(chessboard_size, COLOR_WHITE, TIME)
        self.players = [player1, player2]
        self.chessboard_size = chessboard_size
        self.chessboard = np.zeros((chessboard_size, chessboard_size)).astype('int32')
        self.chessboard[[3, 4], [3, 4]] = COLOR_WHITE
        self.chessboard[[4, 3], [3, 4]] = COLOR_BLACK
        self.turn = COLOR_BLACK
        self.end_mark = 0

    def go(self):
        player = self.players[self.get_index(self.turn)]

        start_time = time.time()
        player.go(self.chessboard)
        end_time = time.time()

        if player.candidate_list:
            row, col = player.candidate_list[-1]
            print(f'-> ({row+1}, {col+1})')
            self.update(row, col)
            self.end_mark = 0
        elif self.end_mark == 0:
            self.end_mark = 1
        else:
            self.end_mark = 2

        if(player.color==-1):
            thistime=end_time-start_time
            global blackstep
            global blacktime
            global blackmaxtime
            if(thistime>blackmaxtime):
                blackmaxtime=thistime
            blacktime+= thistime
            blackstep+=1
        elif(player.color==1):
            thistime= end_time-start_time
            global whitestep
            global whitetime
            global whitemaxtime
            if(thistime>whitemaxtime):
                whitemaxtime=thistime

            whitetime+=end_time-start_time
            whitestep+=1




        print(f'time cost : {end_time - start_time} s','player color:',player.color)

        self.turn *= -1

    def update(self, row, col):
        self.chessboard[row][col] = self.turn
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                i, j = row + dx, col + dy
                step = 0
                while True:
                    if not (0 <= i < self.chessboard_size
                            and 0 <= j < self.chessboard_size) \
                            or self.chessboard[i][j] == COLOR_NONE:
                        break
                    if self.chessboard[i][j] == self.turn:
                        i, j = row + dx, col + dy
                        for k in range(step):
                            self.chessboard[i][j] = self.turn
                            i += dx
                            j += dy
                        break
                    else:
                        i += dx
                        j += dy
                        step += 1

    def statistic(self):
        ret = [0, 0]
        for row in range(self.chessboard_size):
            for col in range(self.chessboard_size):
                idx = (self.chessboard[row, col] + 1) // 2
                ret[idx] += 1
        return ret

    def get_valid_loc(self, color):
        player = self.players[self.get_index(color)]
        player.go(self.chessboard)
        ret = self.chessboard.copy()
        for row, col in player.candidate_list:
            ret[row][col] = color * 2
        return ret

    @staticmethod
    def get_index(color):
        if color == COLOR_BLACK:
            return 0
        elif color == COLOR_WHITE:
            return 1
        else:
            raise ValueError('Color param is not correct')

    def translate_str(self, str_: str):
        lst = str_.replace('[', '').replace(']', '').splitlines()
        size = self.chessboard_size
        ret = np.zeros((size, size)).astype('int32')
        row = 0
        for ss in lst:
            if ss.isspace() or not ss:
                continue
            col = 0
            for s in ss.split(' '):
                if s.isspace() or not s:
                    continue
                ret[row][col] = int(s)
                col += 1
            row += 1
        return ret


if __name__ == '__main__':
    # inner test
    pf = AIPlatform(8)
    # overwrite players

    pf.players[0] = program_current_modify.AI(8, COLOR_BLACK, TIME)      # first one must be black
    pf.players[1] = current_program.AI(8, COLOR_WHITE, TIME)
    start = time.time()


    print(time.time() - start)
#    exit()

    print(pf.chessboard)
    while pf.end_mark != 2:
        pf.go()
        print(pf.chessboard)
    print([player.__class__ for player in pf.players], pf.statistic())
    print("black time:",blacktime,"black step:",blackstep,'avg:',blacktime/(blackstep-1),'blackmaxtime:',blackmaxtime)
    print("white time:",whitetime,"white step:",whitestep,'avg:',whitetime/(whitestep-1),'whitemaxtime:',whitemaxtime)
