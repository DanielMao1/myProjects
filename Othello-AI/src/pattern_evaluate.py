
import numpy as np
from src import data


base_3=[59049, 19683, 6561, 2187, 729, 243, 81, 27, 9, 3, 1]
phase_maps=np.zeros(60,dtype=np.int)
phase_maps[8:33:6]=1
phase_maps[32:61:4]=1



def datainit():
    phase_maps = [None]*61
    phase_maps[8]=data.phase_8()
    phase_maps[14]=data.phase_14()
    phase_maps[20] = data.phase_20()
    phase_maps[26] = data.phase_26()
    phase_maps[32] = data.phase_32()
    phase_maps[36] = data.phase_36()
    phase_maps[40] = data.phase_40()
    phase_maps[44] = data.phase_44()
    phase_maps[48] = data.phase_48()
    phase_maps[52] = data.phase_52()
    phase_maps[56] = data.phase_56()
    phase_maps[60] = data.phase_60()


def loadPhaseMap():
    pass


def evaluate(chessboard,step,side):
    displayed=step
    if(step<8):
        return evaluation_pattern(chessboard,8,side,displayed)
    elif(step==8):
        return evaluation_pattern(chessboard,8,side,displayed)
    elif(step<14):
        weight1=14-step
        weight2=step-8
        total=weight1+weight2
        return (weight1*evaluation_pattern(chessboard,8,side,displayed)+weight2*evaluation_pattern(chessboard,14,side,displayed))/total
    elif(step==14):
        return evaluation_pattern(chessboard,14,side,displayed)
    elif (step < 20):
        weight1 = 20 - step
        weight2 = step - 14
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 14, side,displayed) + weight2 * evaluation_pattern(chessboard, 20,
                                                                                                 side,displayed)) / total
    elif (step == 20):
        return evaluation_pattern(chessboard, 20, side,displayed)
    elif (step < 26):
        weight1 = 26 - step
        weight2 = step - 20
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 20, side,displayed) + weight2 * evaluation_pattern(chessboard, 26,
                                                                                                 side,displayed)) / total
    elif (step == 26):
        return evaluation_pattern(chessboard, 26, side,displayed)
    elif (step < 32):
        weight1 = 32 - step
        weight2 = step - 26
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 26, side,displayed) + weight2 * evaluation_pattern(chessboard, 32,
                                                                                                 side,displayed)) / total
    elif (step==32):
        return evaluation_pattern(chessboard, 32, side,displayed)

    elif (step < 36):
        weight1 = 36 - step
        weight2 = step - 32
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 32, side,displayed) + weight2 * evaluation_pattern(chessboard, 36,
                                                                                                 side,displayed)) / total
    elif (step==36):
        return evaluation_pattern(chessboard, 36, side,displayed)
    elif (step < 40):
        weight1 = 40 - step
        weight2 = step - 36
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 36, side,displayed) + weight2 * evaluation_pattern(chessboard, 40,
                                                                                                 side,displayed)) / total
    elif (step==40):
        return evaluation_pattern(chessboard, 40, side,displayed)
    elif (step < 44):
        weight1 = 44 - step
        weight2 = step - 40
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 40, side,displayed) + weight2 * evaluation_pattern(chessboard, 44,
                                                                                                 side,displayed)) / total
    elif (step==44):
        return evaluation_pattern(chessboard, 44, side,displayed)
    elif (step < 48):
        weight1 = 48 - step
        weight2 = step - 44
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 44, side,displayed) + weight2 * evaluation_pattern(chessboard, 48,
                                                                                                 side,displayed)) / total
    elif (step==48):
        return evaluation_pattern(chessboard, 48, side,displayed)
    elif (step < 52):
        weight1 = 52 - step
        weight2 = step - 48
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 48, side,displayed) + weight2 * evaluation_pattern(chessboard, 52,
                                                                                                  side,displayed)) / total
    elif (step == 52):
        return evaluation_pattern(chessboard, 52, side,displayed)
    elif (step < 56):
        weight1 = 56 - step
        weight2 = step - 52
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 52, side,displayed) + weight2 * evaluation_pattern(chessboard, 56,
                                                                                                  side,displayed)) / total
    elif (step == 56):
        return evaluation_pattern(chessboard, 56, side,displayed)
    elif (step < 60):
        weight1 = 60 - step
        weight2 = step - 56
        total = weight1 + weight2
        return (weight1 * evaluation_pattern(chessboard, 56, side,displayed) + weight2 * evaluation_pattern(chessboard, 60,
                                                                                                  side,displayed)) / total
    else:
        return evaluation_pattern(chessboard, 60, side,displayed)

def colormap(index,power,color):
    if(color==0):
        return index
    else: #白色，2
        big=3**power-1
        return big-index



def evaluation_pattern(chessboard,step,side,displayed)->int:
    phasemapper=phase_maps[step]
    score=0
    score += phasemapper.parity_constant[displayed&1]

    #
    part =np.array([chessboard[72],
    chessboard[22],
    chessboard[81],
    chessboard[71],
    chessboard[61],
    chessboard[51],
    chessboard[41],
    chessboard[31],
    chessboard[21],
    chessboard[11]])
    startLocation=10-len(part)
    base=np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)


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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.cfile[idex]

    part =np.array([ chessboard[68]
    , chessboard[67]
    , chessboard[66]
    , chessboard[65]
    , chessboard[64]
    , chessboard[63]
    , chessboard[62]
    , chessboard[61]])
    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag7[idex]

    part = np.array([[82]
    , chessboard[73]
    , chessboard[64]
    , chessboard[55]
    , chessboard[46]
    , chessboard[37]
    , chessboard[28]])
    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag7[idex]


    part = np.array([[68]
    , chessboard[57]
    , chessboard[46]
    , chessboard[35]
    , chessboard[24]
    , chessboard[13]])
    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag6[idex]

    part = np.array([[86]
    , chessboard[75]
    , chessboard[64]
    , chessboard[53]
    , chessboard[42]
    , chessboard[31]])
    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag6[idex]

    part = np.array([[61]
    , chessboard[52]
    , chessboard[43]
    , chessboard[34]
    , chessboard[25]
    , chessboard[16]])
    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag6[idex]

    part = np.array([[83]
    , chessboard[74]
    , chessboard[65]
    , chessboard[56]
    , chessboard[47]
    , chessboard[38]])

    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag6[idex]

    part = np.array([[58]
    , chessboard[47]
    , chessboard[36]
    , chessboard[25]
    , chessboard[14]])
    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag5[idex]

    part = np.array([[85]
    , chessboard[74]
    , chessboard[63]
    , chessboard[52]
    , chessboard[41]])

    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag5[idex]

    part = np.array([[51]
    , chessboard[42]
    , chessboard[33]
    , chessboard[24]
    , chessboard[15]])

    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag5[idex]


    part = np.array([[84]
    , chessboard[75]
    , chessboard[66]
    , chessboard[57]
    , chessboard[48]])

    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag5[idex]

    part = np.array([[48]
    , chessboard[37]
    , chessboard[26]
    , chessboard[15]])

    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag4[idex]

    part = np.array([[84]
    , chessboard[73]
    , chessboard[62]
    , chessboard[51]])

    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag4[idex]

    part = np.array([[41]
    , chessboard[32]
    , chessboard[23]
    , chessboard[14]])

    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag4[idex]
    part = np.array([[85]
    , chessboard[76]
    , chessboard[67]
    , chessboard[58]])

    startLocation = 10 - len(part)
    base = np.array(base_3[startLocation::])
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.diag4[idex]

    part = np.array([[33]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner33[idex]
    part = np.array([[63]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner33[idex]

    part = np.array([[36]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner33[idex]

    part = np.array([[66]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner33[idex]

    part = np.array([[25]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner52[idex]

    part = np.array([[75]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner52[idex]

    part = np.array([[24]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner52[idex]

    part = np.array([[74]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner52[idex]

    part = np.array([[52]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner52[idex]

    part = np.array([[57]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner52[idex]

    part = np.array([[42]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner52[idex]

    part = np.array([[47]
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
    idex=colormap(base.dot(part),len(part),side)
    score += phasemapper.corner52[idex]
    return score
 