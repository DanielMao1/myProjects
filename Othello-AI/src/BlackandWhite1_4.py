import numpy as np
import random
from src import data

base_3=[19683, 6561, 2187, 729, 243, 81, 27, 9, 3, 1]
# phase_maps=np.zeros(60,dtype=np.int)
# phase_maps[8:33:6]=1
# phase_maps[32:61:4]=1
phase_maps=[None]*61

X_COORDINATE=0
Y_COORDINATE=1
COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(123)
staticMap = np.array([[500,-25,10,5,5,10,-25,500],
                    [-25,-45,1,1,1,1,-45,-25],
                    [10,1,3,2,2,3,1,10],
                    [5,1,2,1,1,2,1,5],
                    [5,1,2,1,1,2,1,5],
                    [10,1,3,2,2,3,1,10],
                    [-25,-45,1,1,1,1,-45,-25],
                    [500,-25,10,5,5,10,-25,500]])
conor=[(0,0),(0,7),(7,0),(7,7)]
star=[(0,1),(1,0),(1,1),
      (1,7),(0,6),(1,6),
      (6,0),(7,1),(6,1),
      (6,7),(7,6),(6,6)]
direction = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
tempboard=np.zeros((8,8))
default_alpha=-100000000
default_beta =100000000



class AI(object):
    phase_maps=[None]*61


 #chessboard_size, color, time_out passed from agent

    def datainit(self):
            self.phase_maps[8] = data.phase_8()
            self.phase_maps[14] = data.phase_14()
            self.phase_maps[20] = data.phase_20()
            self.phase_maps[26] = data.phase_26()
            self.phase_maps[32] = data.phase_32()
            self.phase_maps[36] = data.phase_36()
            self.phase_maps[40] = data.phase_40()
            self.phase_maps[44] = data.phase_44()
            self.phase_maps[48] = data.phase_48()
            self.phase_maps[52] = data.phase_52()
            self.phase_maps[56] = data.phase_56()
            self.phase_maps[60] = data.phase_60()
            return

    def evaluate(self,chessboard, step, side):
     displayed = step
     if (step < 8):
         return self.evaluation_pattern(chessboard, 8, side, displayed)
     elif (step == 8):
         return self.evaluation_pattern(chessboard, 8, side, displayed)
     elif (step < 14):
         weight1 = 14 - step
         weight2 = step - 8
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 8, side, displayed) + weight2 * self.evaluation_pattern(chessboard,
                                                                                                             14, side,
                                                                                                             displayed)) / total
     elif (step == 14):
         return self.evaluation_pattern(chessboard, 14, side, displayed)
     elif (step < 20):
         weight1 = 20 - step
         weight2 = step - 14
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 14, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 20,
             side, displayed)) / total
     elif (step == 20):
         return self.evaluation_pattern(chessboard, 20, side, displayed)
     elif (step < 26):
         weight1 = 26 - step
         weight2 = step - 20
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 20, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 26,
             side, displayed)) / total
     elif (step == 26):
         return self.evaluation_pattern(chessboard, 26, side, displayed)
     elif (step < 32):
         weight1 = 32 - step
         weight2 = step - 26
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 26, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 32,
             side, displayed)) / total
     elif (step == 32):
         return self.evaluation_pattern(chessboard, 32, side, displayed)

     elif (step < 36):
         weight1 = 36 - step
         weight2 = step - 32
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 32, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 36,
             side, displayed)) / total
     elif (step == 36):
         return self.evaluation_pattern(chessboard, 36, side, displayed)
     elif (step < 40):
         weight1 = 40 - step
         weight2 = step - 36
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 36, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 40,
             side, displayed)) / total
     elif (step == 40):
         return self.evaluation_pattern(chessboard, 40, side, displayed)
     elif (step < 44):
         weight1 = 44 - step
         weight2 = step - 40
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 40, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 44,
             side, displayed)) / total
     elif (step == 44):
         return self.evaluation_pattern(chessboard, 44, side, displayed)
     elif (step < 48):
         weight1 = 48 - step
         weight2 = step - 44
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 44, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 48,
             side, displayed)) / total
     elif (step == 48):
         return self.evaluation_pattern(chessboard, 48, side, displayed)
     elif (step < 52):
         weight1 = 52 - step
         weight2 = step - 48
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 48, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 52,
             side, displayed)) / total
     elif (step == 52):
         return self.evaluation_pattern(chessboard, 52, side, displayed)
     elif (step < 56):
         weight1 = 56 - step
         weight2 = step - 52
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 52, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 56,
             side, displayed)) / total
     elif (step == 56):
         return self.evaluation_pattern(chessboard, 56, side, displayed)
     elif (step < 60):
         weight1 = 60 - step
         weight2 = step - 56
         total = weight1 + weight2
         return (weight1 * self.evaluation_pattern(chessboard, 56, side, displayed) + weight2 * self.evaluation_pattern(
             chessboard, 60,
             side, displayed)) / total
     else:
         return self.evaluation_pattern(chessboard, 60, side, displayed)

    def colormap(self,index, power, color):
     if (color == 0):
         return index
     else:  # 白色，2
         big = 3 ** power - 1
         return big - index

    def evaluation_pattern(self,chessboard, step, side, displayed) -> int:
     phasemapper = self.phase_maps[step]
     score = 0
     score += phasemapper.parity_constant[displayed & 1]

     #
     part = np.array([chessboard[72],
                      chessboard[22],
                      chessboard[81],
                      chessboard[71],
                      chessboard[61],
                      chessboard[51],
                      chessboard[41],
                      chessboard[31],
                      chessboard[21],
                      chessboard[11]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)

     score += phasemapper.afile2x[idex]
     #
     part = np.array([chessboard[77],
                      chessboard[27],
                      chessboard[88],
                      chessboard[78],
                      chessboard[68],
                      chessboard[58],
                      chessboard[48],
                      chessboard[38],
                      chessboard[28],
                      chessboard[18]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.afile2x[idex]
     #
     part = np.array([chessboard[27],
                      chessboard[22],
                      chessboard[18],
                      chessboard[17],
                      chessboard[16],
                      chessboard[15],
                      chessboard[14],
                      chessboard[13],
                      chessboard[12],
                      chessboard[11]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.afile2x[idex]
     #
     part = np.array([chessboard[77]
                         , chessboard[72]
                         , chessboard[88]
                         , chessboard[87]
                         , chessboard[86]
                         , chessboard[85]
                         , chessboard[84]
                         , chessboard[83]
                         , chessboard[82]
                         , chessboard[81]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.afile2x[idex]

     part = np.array([chessboard[82]
                         , chessboard[72]
                         , chessboard[62]
                         , chessboard[52]
                         , chessboard[42]
                         , chessboard[32]
                         , chessboard[22]
                         , chessboard[12]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.bfile[idex]

     part = np.array([chessboard[87]
                         , chessboard[77]
                         , chessboard[67]
                         , chessboard[57]
                         , chessboard[47]
                         , chessboard[37]
                         , chessboard[27]
                         , chessboard[17]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.bfile[idex]

     part = np.array([chessboard[28]
                         , chessboard[27]
                         , chessboard[26]
                         , chessboard[25]
                         , chessboard[24]
                         , chessboard[23]
                         , chessboard[22]
                         , chessboard[21]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.bfile[idex]

     part = np.array([chessboard[78]
                         , chessboard[77]
                         , chessboard[76]
                         , chessboard[75]
                         , chessboard[74]
                         , chessboard[73]
                         , chessboard[72]
                         , chessboard[71]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.bfile[idex]

     part = np.array([chessboard[83]
                         , chessboard[73]
                         , chessboard[63]
                         , chessboard[53]
                         , chessboard[43]
                         , chessboard[33]
                         , chessboard[23]
                         , chessboard[13]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.cfile[idex]

     part = np.array([chessboard[86]
                         , chessboard[76]
                         , chessboard[66]
                         , chessboard[56]
                         , chessboard[46]
                         , chessboard[36]
                         , chessboard[26]
                         , chessboard[16]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.cfile[idex]

     part = np.array([chessboard[38]
                         , chessboard[37]
                         , chessboard[36]
                         , chessboard[35]
                         , chessboard[34]
                         , chessboard[33]
                         , chessboard[32]
                         , chessboard[31]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.cfile[idex]

     part = np.array([chessboard[68]
                         , chessboard[67]
                         , chessboard[66]
                         , chessboard[65]
                         , chessboard[64]
                         , chessboard[63]
                         , chessboard[62]
                         , chessboard[61]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.cfile[idex]

     part = np.array([chessboard[84]
                         , chessboard[74]
                         , chessboard[64]
                         , chessboard[54]
                         , chessboard[44]
                         , chessboard[34]
                         , chessboard[24]
                         , chessboard[14]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.dfile[idex]

     part = np.array([chessboard[85]
                         , chessboard[75]
                         , chessboard[65]
                         , chessboard[55]
                         , chessboard[45]
                         , chessboard[35]
                         , chessboard[25]
                         , chessboard[15]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.dfile[idex]

     part = np.array([chessboard[48]
                         , chessboard[47]
                         , chessboard[46]
                         , chessboard[45]
                         , chessboard[44]
                         , chessboard[43]
                         , chessboard[42]
                         , chessboard[41]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.dfile[idex]

     part = np.array([chessboard[58]
                         , chessboard[57]
                         , chessboard[56]
                         , chessboard[55]
                         , chessboard[54]
                         , chessboard[53]
                         , chessboard[52]
                         , chessboard[51]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.dfile[idex]

     part = np.array([chessboard[88]
                         , chessboard[77]
                         , chessboard[66]
                         , chessboard[55]
                         , chessboard[44]
                         , chessboard[33]
                         , chessboard[22]
                         , chessboard[11]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag8[idex]

     part = np.array([chessboard[81]
                         , chessboard[72]
                         , chessboard[63]
                         , chessboard[54]
                         , chessboard[45]
                         , chessboard[36]
                         , chessboard[27]
                         , chessboard[18]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag8[idex]

     part = np.array([chessboard[78]
                         , chessboard[67]
                         , chessboard[56]
                         , chessboard[45]
                         , chessboard[34]
                         , chessboard[23]
                         , chessboard[12]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag7[idex]

     part = np.array([chessboard[87]
                         , chessboard[76]
                         , chessboard[65]
                         , chessboard[54]
                         , chessboard[43]
                         , chessboard[32]
                         , chessboard[21]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag7[idex]

     part = np.array([chessboard[71]
                         , chessboard[62]
                         , chessboard[53]
                         , chessboard[44]
                         , chessboard[35]
                         , chessboard[26]
                         , chessboard[17]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag7[idex]

     part = np.array([chessboard[82]
                         , chessboard[73]
                         , chessboard[64]
                         , chessboard[55]
                         , chessboard[46]
                         , chessboard[37]
                         , chessboard[28]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     why=base.dot(part)
     idex = self.colormap(why, len(part), side)
     score += phasemapper.diag7[idex]

     part = np.array([chessboard[68]
                         , chessboard[57]
                         , chessboard[46]
                         , chessboard[35]
                         , chessboard[24]
                         , chessboard[13]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag6[idex]

     part = np.array([chessboard[86]
                         , chessboard[75]
                         , chessboard[64]
                         , chessboard[53]
                         , chessboard[42]
                         , chessboard[31]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag6[idex]

     part = np.array([chessboard[61]
                         , chessboard[52]
                         , chessboard[43]
                         , chessboard[34]
                         , chessboard[25]
                         , chessboard[16]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag6[idex]

     part = np.array([chessboard[83]
                         , chessboard[74]
                         , chessboard[65]
                         , chessboard[56]
                         , chessboard[47]
                         , chessboard[38]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag6[idex]

     part = np.array([chessboard[58]
                         , chessboard[47]
                         , chessboard[36]
                         , chessboard[25]
                         , chessboard[14]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag5[idex]

     part = np.array([chessboard[85]
                         , chessboard[74]
                         , chessboard[63]
                         , chessboard[52]
                         , chessboard[41]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag5[idex]

     part = np.array([chessboard[51]
                         , chessboard[42]
                         , chessboard[33]
                         , chessboard[24]
                         , chessboard[15]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag5[idex]

     part = np.array([chessboard[84]
                         , chessboard[75]
                         , chessboard[66]
                         , chessboard[57]
                         , chessboard[48]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag5[idex]

     part = np.array([chessboard[48]
                         , chessboard[37]
                         , chessboard[26]
                         , chessboard[15]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag4[idex]

     part = np.array([chessboard[84]
                         , chessboard[73]
                         , chessboard[62]
                         , chessboard[51]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag4[idex]

     part = np.array([chessboard[41]
                         , chessboard[32]
                         , chessboard[23]
                         , chessboard[14]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag4[idex]
     part = np.array([chessboard[85]
                         , chessboard[76]
                         , chessboard[67]
                         , chessboard[58]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.diag4[idex]

     part = np.array([chessboard[33]
                         , chessboard[32]
                         , chessboard[31]
                         , chessboard[23]
                         , chessboard[22]
                         , chessboard[21]
                         , chessboard[13]
                         , chessboard[12]
                         , chessboard[11]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner33[idex]
     part = np.array([chessboard[63]
                         , chessboard[62]
                         , chessboard[61]
                         , chessboard[73]
                         , chessboard[72]
                         , chessboard[71]
                         , chessboard[83]
                         , chessboard[82]
                         , chessboard[81]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner33[idex]

     part = np.array([chessboard[36]
                         , chessboard[37]
                         , chessboard[38]
                         , chessboard[26]
                         , chessboard[27]
                         , chessboard[28]
                         , chessboard[16]
                         , chessboard[17]
                         , chessboard[18]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner33[idex]

     part = np.array([chessboard[66]
                         , chessboard[67]
                         , chessboard[68]
                         , chessboard[76]
                         , chessboard[77]
                         , chessboard[78]
                         , chessboard[86]
                         , chessboard[87]
                         , chessboard[88]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner33[idex]

     part = np.array([chessboard[25]
                         , chessboard[24]
                         , chessboard[23]
                         , chessboard[22]
                         , chessboard[21]
                         , chessboard[15]
                         , chessboard[14]
                         , chessboard[13]
                         , chessboard[12]
                         , chessboard[11]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner52[idex]

     part = np.array([chessboard[75]
                         , chessboard[74]
                         , chessboard[73]
                         , chessboard[72]
                         , chessboard[71]
                         , chessboard[85]
                         , chessboard[84]
                         , chessboard[83]
                         , chessboard[82]
                         , chessboard[81]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner52[idex]

     part = np.array([chessboard[24]
                         , chessboard[25]
                         , chessboard[26]
                         , chessboard[27]
                         , chessboard[28]
                         , chessboard[14]
                         , chessboard[15]
                         , chessboard[16]
                         , chessboard[17]
                         , chessboard[18]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner52[idex]

     part = np.array([chessboard[74]
                         , chessboard[75]
                         , chessboard[76]
                         , chessboard[77]
                         , chessboard[78]
                         , chessboard[84]
                         , chessboard[85]
                         , chessboard[86]
                         , chessboard[87]
                         , chessboard[88]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner52[idex]

     part = np.array([chessboard[52]
                         , chessboard[42]
                         , chessboard[32]
                         , chessboard[22]
                         , chessboard[12]
                         , chessboard[51]
                         , chessboard[41]
                         , chessboard[31]
                         , chessboard[21]
                         , chessboard[11]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner52[idex]

     part = np.array([chessboard[57]
                         , chessboard[47]
                         , chessboard[37]
                         , chessboard[27]
                         , chessboard[17]
                         , chessboard[58]
                         , chessboard[48]
                         , chessboard[38]
                         , chessboard[28]
                         , chessboard[18]])
     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner52[idex]

     part = np.array([chessboard[42]
                         , chessboard[52]
                         , chessboard[62]
                         , chessboard[72]
                         , chessboard[82]
                         , chessboard[41]
                         , chessboard[51]
                         , chessboard[61]
                         , chessboard[71]
                         , chessboard[81]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner52[idex]

     part = np.array([chessboard[47]
                         , chessboard[57]
                         , chessboard[67]
                         , chessboard[77]
                         , chessboard[87]
                         , chessboard[48]
                         , chessboard[58]
                         , chessboard[68]
                         , chessboard[78]
                         , chessboard[88]])

     startLocation = 10 - len(part)
     base = np.array(base_3[startLocation::])
     idex = self.colormap(base.dot(part), len(part), side)
     score += phasemapper.corner52[idex]
     return score
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        self.color = color
        self.candidate_list = []
        self.datainit()


    def makemove(self,move,side,chessboard)->list:
        chessboard[move[0]][move[1]]=side
        flippedChess=self.flipChess(move,side,chessboard)
        return flippedChess

    def unmakemove(self,move,side,chessboard,flippedchess):
        chessboard[move[0]][move[1]] = COLOR_NONE
        for chess in flippedchess:
            chessboard[chess[0]][chess[1]]=-side
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

    def go(self, chessboard):

            self.candidate_list.clear()
            myColor = self.color
            opponentColor = -self.color

            empty = np.where(chessboard == COLOR_NONE)
            empty = list((zip(empty[0], empty[1])))
            rest_step=empty.__len__()
            stage=60-rest_step
            available_moves=self.findavailable(chessboard,myColor,empty)#这个和candidate_list是一个引用
            if(available_moves.__len__()==0):
                return self.candidate_list

            #开始搜索
            bestmove=self.rootSearch(self.candidate_list,myColor,chessboard,2,stage)
            self.candidate_list.append(bestmove)
            return self.candidate_list



    def findavailable(self,chessboard,myColor,empty):
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
                        break
        return self.candidate_list

    def rootSearch(self,real_candidate_list,side,chessboard,depth,step):
        if(real_candidate_list.__len__()>0):
            bestmove=real_candidate_list[real_candidate_list.__len__()-1]
            bestscore=-999999
            scores=[]
            for move in real_candidate_list:
                flipped=self.makemove(move,side,chessboard)
                score=-self.subsearch(-side,chessboard,depth-1,default_alpha,default_beta,side,step+1)#应该返回一个
                #print("score returned:",score)
                if(score>bestscore):
                    bestscore = score
                    bestmove  = move
                    self.candidate_list.append(move)
                self.unmakemove(move,side,chessboard,flipped)
                scores.append(score)
            print("the score list:",scores,"movelist:",real_candidate_list,"best score:",bestscore,",best move:",(bestmove[0],bestmove[1]))
            return bestmove
        return
    #将二维棋盘映射成为一维棋盘
    def two_to_one_map(self,two_demension_board):
        one_demention_board=np.array([3]*89)
        for i in range(0,8):
            for j in range(0,8):
                if(two_demension_board[i][j]==COLOR_BLACK):
                    one_demention_board[(i+1)*10+(j+1)]=0
                elif(two_demension_board[i][j]==COLOR_WHITE):
                    one_demention_board[(i + 1) * 10 + (j + 1)] = 2
                else:
                    one_demention_board[(i + 1) * 10 + (j + 1)]=1
        return one_demention_board



    #def makemove_onedimension(self):



    def subsearch(self,side,chessboard,depth,alpha,beta,myside,step)->int:
        mymax=-1000000000
        if (depth <= 0):
            if(side==myside):
                return self.evaluate(self.two_to_one_map(chessboard),step,side+1)#如果是白，1变2，如果是黑，-1变0
            else:
                return -self.evaluate(self.two_to_one_map(chessboard),step,side+1)
        else:
            mylist=self.getMoves(chessboard,side)

            if(mylist.__len__()>0):
                for valid_move in mylist:
                    flipped=self.makemove(valid_move,side,chessboard)
                    score=-self.subsearch(-side,chessboard,depth-1,-beta,-alpha,myside,step+1)
                    self.unmakemove(valid_move,side,chessboard,flipped)
                    if(score>alpha):
                        alpha = score
                        if(score>beta):#剪枝，如果是初始值，score永远不会大于beta
                            return score
                    if(score>mymax):
                        mymax=score
                return mymax
            else:
                opponent_list = self.getMoves(chessboard, -side)
                if(opponent_list.__len__()==0):
                    (blackscore,whitescore)=self.getBothScore(chessboard)
                    return 1000000*(-myside)*(blackscore-whitescore)
                else:
                    return -self.subsearch(-side,chessboard,depth,-beta,-alpha,myside,step)

    def map1(chessboard, myside):
        return sum(sum(chessboard * staticMap)) * myside


    def getBothScore(self,board)->(int,int):
        blackScore = np.where(board == COLOR_BLACK).__len__()
        whiteScore = np.where(board == COLOR_WHITE).__len__()
        # print("blackScore:",blackScore,",whiteScore:",whiteScore)
        return (blackScore, whiteScore)


