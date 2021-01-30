import numpy as np
arr=np.array([0,1,2,3,4,5])
print(arr)

def find_narcissistic_number(start: int, end: int)->list:
    list=[]
    if(start<=end):
        for i in range(start,end+1):
            str_1=str(i)
            length=len(str_1)
            sum=0
            for j in str_1:
                sum+=int(j)**length
            if(sum==i):
                list.append(i)
        return list
    else:
        return list

list2=find_narcissistic_number(1,1000000)
for i in list2:
    print(i)


