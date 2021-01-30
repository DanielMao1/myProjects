from src import  data
import numpy as np


def totextclass():
    phases = data.bitmaps
    file = open('bytefile.txt', 'a+')
    for i in range(0,61):
        data.initia(i)

    for j in range(0,61):
        if(phases[j].permanent==1):
            multiply(phases[j], 2)
            print("if(x==%d):"%(j),file =file)
            print("\tbitmaps[%d].parity_constant ="%(j),phases[j].parity_constant,file =file)
            print("\tbitmaps[%d].afile2x ="%(j),phases[j].afile2x,file =file)
            print("\tbitmaps[%d].bfile ="%(j),phases[j].bfile,file =file)
            print("\tbitmaps[%d].cfile ="%(j),phases[j].cfile,file =file)
            print("\tbitmaps[%d].dfile ="%(j),phases[j].dfile,file =file)
            print("\tbitmaps[%d].diag8 ="%(j),phases[j].diag8,file =file)
            print("\tbitmaps[%d].diag7 ="%(j),phases[j].diag7,file =file)
            print("\tbitmaps[%d].diag6 ="%(j),phases[j].diag6,file =file)
            print("\tbitmaps[%d].diag5 ="%(j),phases[j].diag5,file =file)
            print("\tbitmaps[%d].diag4 ="%(j),phases[j].diag4,file =file)
            print("\tbitmaps[%d].corner33 ="%(j),phases[j].corner33,file =file)
            print("\tbitmaps[%d].corner52 ="%(j),phases[j].corner52,file =file)
            print(file =file)
            file.flush()
    file.close()

def tobyteclass():
    phases = data.bitmaps
    file = open('bytefile.txt', 'a+')

    for i in range(0,61):
        data.initia(i)

    for j in range(0,61):
        if(phases[j].permanent==1):
            multiply(phases[j], 1)
            print("if(x==%d):"%(j),file =file)
            print("\tbitmaps[%d].parity_constant ="%(j),phases[j].parity_constant.tobytes(),file =file)
            print("\tbitmaps[%d].afile2x ="%(j),str(phases[j].afile2x.tobytes()),file =file)
            print("\tbitmaps[%d].bfile ="%(j),str(phases[j].bfile.tobytes()),file =file)
            print("\tbitmaps[%d].cfile ="%(j),str(phases[j].cfile.tobytes()),file =file)
            print("\tbitmaps[%d].dfile ="%(j),str(phases[j].dfile.tobytes()),file =file)
            print("\tbitmaps[%d].diag8 ="%(j),str(phases[j].diag8.tobytes()),file =file)
            print("\tbitmaps[%d].diag7 ="%(j),str(phases[j].diag7.tobytes()),file =file)
            print("\tbitmaps[%d].diag6 ="%(j),str(phases[j].diag6.tobytes()),file =file)
            print("\tbitmaps[%d].diag5 ="%(j),str(phases[j].diag5.tobytes()),file =file)
            print("\tbitmaps[%d].diag4 ="%(j),str(phases[j].diag4.tobytes()),file =file)
            print("\tbitmaps[%d].corner33 ="%(j),str(phases[j].corner33.tobytes()),file =file)
            print("\tbitmaps[%d].corner52 ="%(j),str(phases[j].corner52.tobytes()),file =file)
            print(file =file)
            file.flush()
    file.close()


def tobyteclass_signgle(indexlist):
    phases = data.bitmaps
    file = open('bytefile.py', 'a+')

    for i in range(0, 61):
        data.initia(i)

    for index in indexlist:
        if (phases[index].permanent == 1):
                multiply(phases[index], 1)
                print("if(x==%d):" % (index), file=file)
                print("\tbitmaps[%d].parity_constant =np.frombnp.frombuffer(" % (index), phases[index].parity_constant.tobytes(), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].afile2x =np.frombuffer(" % (index), str(phases[index].afile2x.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].bfile =np.frombuffer(" % (index), str(phases[index].bfile.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].cfile =np.frombuffer(" % (index), str(phases[index].cfile.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].dfile =np.frombuffer(" % (index), str(phases[index].dfile.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].diag8 =np.frombuffer(" % (index), str(phases[index].diag8.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].diag7 =np.frombuffer(" % (index), str(phases[index].diag7.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].diag6 =np.frombuffer(" % (index), str(phases[index].diag6.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].diag5 =np.frombuffer(" % (index), str(phases[index].diag5.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].diag4 =np.frombuffer(" % (index), str(phases[index].diag4.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].corner33 =np.frombuffer(" % (index), str(phases[index].corner33.tobytes()), ",dtype=np.int16)",file=file)
                print("\tbitmaps[%d].corner52 =np.frombuffer(" % (index), str(phases[index].corner52.tobytes()), ",dtype=np.int16)",file=file)
                print(file=file)
                file.flush()
    file.close()
def multiply(ob,factor):

    ob.parity_constant=np.right_shift(ob.parity_constant,factor)
    ob.afile2x=np.right_shift(ob.afile2x , factor)
    ob.bfile=np.right_shift(ob.bfile , factor)
    ob.cfile=np.right_shift(ob.cfile , factor)
    ob.dfile=np.right_shift(ob.dfile , factor)
    ob.diag8=np.right_shift(ob.diag8 , factor)
    ob.diag7=np.right_shift(ob.diag7 , factor)
    ob.diag6= np.right_shift(ob.diag6 , factor)
    ob.diag5=np.right_shift(ob.diag5 , factor)
    ob.diag4=np.right_shift(ob.diag4 , factor)
    ob.corner33=np.right_shift(ob.corner33 , factor)
    ob.corner52=np.right_shift(ob.corner52 , factor)

def totextclass_single(indexlist):
        phases = data.bitmaps
        file = open('bytefile.txt', 'a+')
        for i in range(0,61):
            data.initia(i)
        for index in indexlist:
            if(phases[index].permanent==1):
                multiply(phases[index], 1)
                print("if(x==%d):"%(index),file =file)
                print("\tbitmaps[%d].parity_constant = ["%(index),",".join(str(k) for k in phases[index].parity_constant),"]",file =file)
                print("\tbitmaps[%d].afile2x = ["%(index),",".join(str(k) for k in phases[index].afile2x),"]",file =file)
                print("\tbitmaps[%d].bfile = ["%(index), ",".join(str(k) for k in phases[index].bfile),"]",file =file)
                print("\tbitmaps[%d].cfile = ["%(index),",".join(str(k) for k in phases[index].cfile),"]",file =file)
                print("\tbitmaps[%d].dfile = ["%(index),",".join(str(k) for k in phases[index].dfile),"]",file =file)
                print("\tbitmaps[%d].diag8 = ["%(index),",".join(str(k) for k in phases[index].diag8),"]",file =file)
                print("\tbitmaps[%d].diag7 = ["%(index),",".join(str(k) for k in phases[index].diag7),"]",file =file)
                print("\tbitmaps[%d].diag6 = ["%(index),",".join(str(k) for k in phases[index].diag6),"]",file =file)
                print("\tbitmaps[%d].diag5 = ["%(index),",".join(str(k) for k in phases[index].diag5),"]",file =file)
                print("\tbitmaps[%d].diag4 = ["%(index),",".join(str(k) for k in phases[index].diag4),"]",file =file)
                print("\tbitmaps[%d].corner33 = ["%(index),",".join(str(k) for k in phases[index].corner33),"]",file =file)
                print("\tbitmaps[%d].corner52 = ["%(index),",".join(str(k) for k in phases[index].corner52),"]",file =file)
                print(file =file)
                file.flush()
        file.close()

def generrate_final_data(textlist,bytelist):
        totextclass_single(textlist)
        tobyteclass_signgle(bytelist)




tobyteclass_signgle([40,44,48,52,56])
# generrate_final_data([],)





# class bitmap:
#     permanent = 0
#     parity_constant = None
#     afile2x = None
#     bfile = None
#     cfile = None
#     dfile = None
#     diag8 = None
#     diag7 = None
#     diag5 = None
#     diag6 = None
#     diag4 = None
#     corner33 = None
#     corner52 = None


# bitmaps = [bitmap] * 61
# print(bitmaps)
#
# bitmaps[0].diag4
