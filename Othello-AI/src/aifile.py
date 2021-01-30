import numpy as np
from src import data_numpy


#phase_8 = data_numpy.phase_8()
#phase_20  = data_numpy.phase_20()
#phase_48 = data_numpy.phase_48()
#phase_48  = data_numpy.phase_48()
#phase_48 = data_numpy.phase_48()
#phase_48  = data_numpy.phase_48()
# phase_48 = data_numpy.phase_48()
phase_48 = data_numpy.phase_48()
file =open('bytefile.txt','a+')
print('class phase_48:\n',file =file)
print('\tparity_constant =',phase_48.parity_constant.tobytes(),file =file)
print('\tafile2x =',phase_48.afile2x.tobytes(),file =file)
print('\tbfile =',phase_48.bfile.tobytes(),file =file)
print('\tcfile =',phase_48.cfile.tobytes(),file =file)
print('\tdfile =',phase_48.dfile.tobytes(),file =file)
print('\tdiag8 =',phase_48.diag8.tobytes(),file =file)
print('\tdiag7 =',phase_48.diag7.tobytes(),file =file)
print('\tdiag6 =',phase_48.diag6.tobytes(),file =file)
print('\tdiag5 =',phase_48.diag5.tobytes(),file =file)
print('\tdiag4 =',phase_48.diag4.tobytes(),file =file)
print('\tcorner33 =',phase_48.corner33.tobytes(),file =file)
print('\tcorner52 =',phase_48.corner52.tobytes(),file =file)
print(file =file)
file.close()

