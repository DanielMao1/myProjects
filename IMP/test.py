import numpy as np
import random
import time
import argparse

sum=0
log=False

def attemptActivate(node:int,weight:float)->bool:
    possible=random.random()
    if(log):
        print("节点%d有%f的概率被激活"%(node,weight))
        print("本次随机数为：",possible)
    if(0<=possible<=weight):
        return True
    else:
        return False

def attemptActivateLT(node:int,weight:float)->bool:
    possible=random.random()
    print("节点%d有%f的概率被激活"%(node,weight))
    print("本次随机数为：",possible)
    if(0<=possible<=weight):
        return True
    else:
        return False

def main():
    '''
    从命令行读参数示例
    '''

    #print("从命令行读参数示例")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--file_name', type=str, default='network.txt')
    parser.add_argument('-s', '--seed', type=str, default='network_seeds.txt')
    parser.add_argument('-m', '--model', type=str, default='IC')
    parser.add_argument('-t', '--time_limit', type=int, default=60)

    args = parser.parse_args()
    file_name = args.file_name
    seed = args.seed
    model = args.model
    time_limit = args.time_limit


    #print(file_name, seed, model, time_limit)
    totalTime=0
    overhead=4

    global sum
    interate_times=0
    sum=0
    seedSet,nodesActivity,outDict,inDict,nodeNum=initGraph(file_name,seed)
    if(model=='IC'):
        while totalTime<=time_limit-overhead:

            timestart=time.time()
            ICmode(seedSet.copy(),nodesActivity.copy(),outDict,inDict)
            timeend=time.time()
            totalTime+=timeend-timestart
            interate_times+=1
        if(log):
            print("IC平均激活数：%f"%(sum/interate_times))
        else:
            print(sum/interate_times)
    else:
        while totalTime <= time_limit - overhead:
            timestart = time.time()
            LTmode(seedSet.copy(),nodesActivity.copy(),outDict,inDict,nodeNum)
            timeend = time.time()
            totalTime += timeend - timestart
            interate_times+=1
        if(log):
            print("LT平均激活数：%f"%(sum/interate_times))
        else:
            print(sum/interate_times)
    if(log):
        print("迭代次数：",interate_times,"运行时间:",totalTime)





class Edge():
    def __init__(self,outnode:int,innode:int,weight:float):
        self.outnode=outnode
        self.innode=innode
        self.weight=weight

def initGraph(graphPath,seedPath):
    # graphPath="D:\\courseStation\\CS303\\Project2\\network.txt"
    # seedPath="D:\\courseStation\\CS303\\Project2\\network_seeds.txt"
    #构造图
    graphFile=open(graphPath,mode="r")
    str=graphFile.read()
    graphFile.close()
    str=str.strip()
    strsplit=str.split("\n")
    parameters=strsplit[0].split(" ")
    if(log):
        print(int(parameters[0]),int(parameters[1]))
    nodenum=int(parameters[0])
    edgenum=int(parameters[1])
    nodesActivity=np.zeros(nodenum+1)
    outDict={}
    inDict={}
    for i in range(1,strsplit.__len__()):
        start,end,weight=strsplit[i].split(" ")
        start=int(start)
        end=int(end)
        weight=float(weight)
        edge=Edge(start,end,weight)

        outNodeEdges=outDict.setdefault(start, [])
        inNodeEdges=inDict.setdefault(end, [])
        outNodeEdges.append(edge)
        inNodeEdges.append(edge)
    #构造激活集合
    seedFile=open(seedPath,mode="r")
    strSeed=seedFile.read().strip()
    seedFile.close()
    strsplit=strSeed.split("\n")

    seedSet=[]
    for i in strsplit:
        nodeIndex=int(i)
        seedSet.append(nodeIndex)
        nodesActivity[nodeIndex]=1#激活种子

    return seedSet,nodesActivity,outDict,inDict,nodenum

def ICmode(seedSet,nodeActivity,outDict,inDict):
    global sum
    count = seedSet.__len__()
    if(log):
        print("初始化：",seedSet,nodeActivity,outDict,inDict)
    while(seedSet.__len__()>0):
        newActivitySet=[]

        for node in seedSet:
            if(log):
                print("对于节点",node,":")
            neighbours=outDict.get(node,[])
            if(log):
                print("邻居有：")
                for i in neighbours:
                    print(i)

            for edge in neighbours:
                if(nodeActivity[edge.innode]==0):
                    if(attemptActivate(edge.innode,edge.weight)):
                        if(log):
                            print("节点",edge.innode,"被激活了！")
                        nodeActivity[edge.innode]=1
                        newActivitySet.append(edge.innode)
        count+=newActivitySet.__len__()
        seedSet.clear()#是否能够节约内存？
        seedSet=newActivitySet
    if(log):
        print("本次激活：%d"%count)
    sum+=count

def LTmode(seedSet,nodeActivity,outDict,inDict,nodeNum):
    global sum
    count = seedSet.__len__()
    nodeThresholds=[]
    nodeWeight=[0]*(nodeNum+1)
    for i in range(0,nodeNum+1):
        nodeThresholds.append(random.random())
    if(log):
        print("初始化：",seedSet,nodeActivity,outDict,inDict)
    while(seedSet.__len__()>0):
        newActivitySet=[]

        for node in seedSet:
            neighbours = outDict.get(node, [])
            if(log):
                print("对于节点",node,":")
                print("邻居有：")
                for i in neighbours:
                    print(i)





            for edge in neighbours:
                if(nodeActivity[edge.innode]==0):
                    nodeWeight[edge.innode]+=edge.weight
                    if(nodeWeight[edge.innode]>=nodeThresholds[edge.innode]):
                        if(log):
                            print("节点",edge.innode,"被激活了！")
                        nodeActivity[edge.innode]=1
                        newActivitySet.append(edge.innode)
        count+=newActivitySet.__len__()
        seedSet.clear()#是否能够节约内存？
        seedSet=newActivitySet
    if(log):
        print("本次激活：%d"%count)
    sum+=count

if __name__ == '__main__':
    main()









# for (key,value) in dictOut.items():
#     print(key,value)
# for j in dictIn.items():
#     print(j)







# for i in range(1,edgenum+1):
#
#     print(i)

