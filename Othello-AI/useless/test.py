

def isleapYear(year):
    if(year%4!=0):
        return False
    elif(year%100!=0):
        return True
    elif(year%400!=0):
        return False
    else:
        return True

def day(x,year,month,day):
    mon=[31,28,31,30,31,30,31,31,30,31,30,31]
    offset=0
    for i in range (1,year):
        leap = isleapYear(i)
        if leap:
            offset= (offset+366)%x
        else:
            offset=(offset+365)%x
    offset%=x
    leap=isleapYear(year)
    if(leap):
        mon[1]=29
    for i in range(0,month-1):
        offset=(offset+mon[i])%x
    offset=(offset+day)%x
    if(offset==0):
        print(x)
    else:
        print(offset)
day(16,17504,8,18)











