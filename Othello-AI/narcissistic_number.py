
def find_narcissistic_number(start: int, end: int) -> list:
    list=[]
    if(start<end):
        for i in range(start,end):
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


