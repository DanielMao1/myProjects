

import numpy as np
import random
import time
import argparse
import multiprocessing as mp
import sys
import os
import math
sum=0
core=4
log=False
log2=True
time_factor=0.5

class Processor(mp.Process):
    def __init__(self, outQ, theta,V,diffusion_model,rev_adj_graph):
        super(Processor, self).__init__(target=self.start)
        self.V=V
        self.diffusion_model=diffusion_model
        self.rev_adj_graph=rev_adj_graph
        self.outQ = outQ
        self.R = []
        self.theta = theta

    def run(self):
        count = 0
        while count < self.theta:
            v = random.randint(1, self.V)
            if self.diffusion_model == 'IC':
                rr = get_rr([v],self.rev_adj_graph)
            else:
                rr = get_rr_lt([v],self.rev_adj_graph)
            self.R.append(rr)
            count += 1
        self.outQ.put(self.R)

def attemptActivate(node:int,weight:float)->bool:
    possible=random.random()
    if(log):
        print("节点%d有%f的概率被激活"%(node,weight))
        print("本次随机数为：",possible)
    if(0<=possible<=weight):
        return True
    else:
        return False
class Edge():
    def __init__(self,outnode:int,innode:int,weight:float):
        self.outnode=outnode
        self.innode=innode
        self.weight=weight


def initReverseGraph(graphPath):
    """
    :param graphPath:
    :return:
    nodenum: number of node, index from 1
    outDict: int:list dictionary, the edge of certain node
    edgenum: the number of edges
    """
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
    #inDict={}
    for i in range(1,strsplit.__len__()):
        start,end,weight=strsplit[i].split(" ")
        start=int(start)
        end=int(end)
        weight=float(weight)
        #反向边
        edge = Edge(end, start, weight)
        #这是正向边
        #edge=Edge(start,end,weight)
        outNodeEdges=outDict.setdefault(end, [])
        #inNodeEdges=inDict.setdefault(start, [])
        outNodeEdges.append(edge)
        #inNodeEdges.append(edge)
    return nodenum,outDict,edgenum

def nodeSelection_revise(setR,k,nodeNum):

    skset=set()
    nodeAndReachableMap=dict()
    nodeLengthMap = dict()
    # i=0
    # setR_len=len(setR)
    for rrindex in range(0,len(setR)):
        currentRR=setR[rrindex]
        for node in currentRR:
           # nodeCover[node]+=1
            if node not in nodeAndReachableMap.keys():
                nodeAndReachableMap[node]=set()
            nodeAndReachableMap[node].add(rrindex)
    for node in nodeAndReachableMap:
        nodeLengthMap[node]=len(nodeAndReachableMap[node])

    # for node in nodeAndReachableMap.keys():
    #     nodeCover[node]=len(nodeAndReachableMap[node])

    for i in range(0,k):
        max_node=None
        maxNodeCoverNum=-1
        for node in  nodeLengthMap:
            coverNum=nodeLengthMap[node]
            if coverNum>maxNodeCoverNum:
                maxNodeCoverNum=coverNum
                max_node=node
        if(max_node !=None):
            skset.add(max_node)
            #数组复制
            for rr_index in nodeAndReachableMap[max_node]:
                currentRR=setR[rr_index]
            #对于每一个被max_node覆盖到的rr，删除
                for node in currentRR:
                    if(node==max_node):
                        continue
                    nodeLengthMap[node]-=1#其它节点删除rr的影响
                    nodeAndReachableMap[node].remove(rr_index)#在node列表中删除rr
            del[nodeAndReachableMap[max_node]]
            del[nodeLengthMap[max_node]]
        else:
            while 1:
                nextNode=random.randint(1,nodeNum)
                if(nextNode not in skset):
                    skset.add(nextNode)
                    break

    return skset

def nodeSelection(setR,k,nodeNum):
    skset=set()
    nodeAndReachableMap=dict()
    nodeLengthMap=dict()
    #nodeInRRLengthMap=dict()
    nodeCover = [0 for i in range(0, nodeNum + 1)]
    for rrindex in range(0,len(setR)):
        currentRR=setR[rrindex]
        for node in currentRR:
            nodeCover[node]+=1
            if node not in nodeAndReachableMap.keys():
                nodeAndReachableMap[node]=[]
            nodeAndReachableMap[node].append(rrindex)


    # for node in nodeAndReachableMap.keys():
    #     nodeCover[node]=len(nodeAndReachableMap[node])

    while 1:
        if(skset.__len__()==k):
            break
        max_node=nodeCover.index(max(nodeCover))
        skset.add(max_node)

        rr_covered=[]
        #数组复制
        for rr in nodeAndReachableMap[max_node]:
            rr_covered.append(rr)
        #对于每一个被max_node覆盖到的rr，删除
        for rrindex in rr_covered:
            rr=setR[rrindex]
            for node in rr:
                nodeCover[node]-=1#其它节点删除rr的影响
                nodeAndReachableMap[node].remove(rrindex)#在node列表中删除rr
    return skset

def imp():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--file_name', type=str, default='network.txt')
    parser.add_argument('-k', '--seedNum', type=int, default=5)
    parser.add_argument('-m', '--model', type=str, default='IC')
    parser.add_argument('-t', '--time_limit', type=int, default=60)
    args = parser.parse_args()
    file_name = args.file_name
    seedNum = args.seedNum
    model = args.model
    time_limit = args.time_limit
    # 1.ℓ = ℓ · (1 + log 2 / log n);
    # 2.R = Sampling(G, k, ε, ℓ);
    #跳过
    graphPath = file_name
    nodes, outDict, edgenum=initReverseGraph(graphPath)



    if(log):
        print("生成可达集开始...")
    pool = mp.Pool(core)
    setR = []
    time_start=time.time()
    result=[]
    for i in range(core):
        result.append(pool.apply_async(getRRs, args=(nodes,outDict,model,time_limit*time_factor,time_start)))

    pool.close()


    timeCloseStart = time.time()
    print("join开始：",timeCloseStart)
    pool.join()
    timeCloseEnd = time.time()
    print("join结束：",timeCloseEnd)
    print("join所花时间:", timeCloseEnd - timeCloseStart)
    extendStart=time.time()
    for process in result:
        setR.extend(process.get())
    extendEnd=time.time()
    print("这个时间好长啊",extendEnd-extendStart)
    time_end=time.time()
    #setR=getRRs(nodes,outDict,model,time_limit*1/2)
    if(log2):
        print("生成的集合数量：",len(setR))
        print("time_end：",time_end)
        print("生成集合所花时间：",time_end-time_start)
    setSk=nodeSelection_revise(setR,seedNum,nodes)
    for node in setSk:
        print(node)
    sys.stdout.flush()

    # 3.S∗k= NodeSelection(R, k);
    # 4.return S∗
def getRRs(nodeNum,outDict,model,time_limit,global_time_start):

    if(log2):
        print("时间上限：",time_limit)
        print("全局开始时间：",global_time_start)
        print("进程：", os.getpid())
    setR=[]
    totalTime=0
    loopNum=0
    if (model == 'IC'):
        while 1:
            if(log):
                loopNum+=1
                print("第%d次循环开始"%(loopNum))
            #timeStart=time.time()
            nodeV=random.randint(1,nodeNum)
            if(log):
                print("生成 %d 号节点的可达集"%(nodeV))
            currentReachableSet=justgetRR_IC(nodeV,outDict)
            setR.append(currentReachableSet)
            timeEnd=time.time()
            timeFly=timeEnd-global_time_start
            #totalTime+=timeEnd-timeStart
            #if(log):
                #print("花费时间:",totalTime)
            if(timeFly>time_limit):
                break
    else:
        while 1:
            timeStart=time.time()
            nodeV=random.randint(1,nodeNum)

            currentReachableSet=justgetRR_LT(nodeV,outDict)
            if(log):
                print("生成 %d 号节点的可达集"%(nodeV))
                print("可达集信息:",currentReachableSet)
            setR.append(currentReachableSet)
            timeEnd=time.time()
            totalTime+=timeEnd-timeStart
            if(log):
                print("花费时间:",totalTime)
            timeEnd=time.time()
            timeFly=timeEnd-global_time_start
            #totalTime+=timeEnd-timeStart
            #if(log):
                #print("花费时间:",totalTime)
            if(timeFly>time_limit):
                break
    if(log2):
        print("结束时间:", time.time())
    return setR







# def sampling(graph,k,epsilong,l,nodenum):
#     epsilong_plus=1.414*epsilong
#     for i in range(1,int(math.log(nodenum,2))-1):
#         x=nodenum/2**i
#
#     pass
def justgetRR_IC(nodeV, outDict):
    reverse_reachable_set=set()
    activeSet=set()
    nodeSet=[nodeV]
    for node in nodeSet:
        activeSet.add(node)
        reverse_reachable_set.add(node)
    while activeSet.__len__()!=0:
        newActiveSet=set()
        for node in activeSet:
            neighbours=outDict.get(node,[])
            #加个log
            for edge in neighbours:
                if edge.innode not in reverse_reachable_set and edge.innode not in newActiveSet and  attemptActivate(edge.innode,edge.weight):
                    newActiveSet.add(edge.innode)
        activeSet.clear()
        activeSet=newActiveSet
        reverse_reachable_set=reverse_reachable_set.union(newActiveSet)
    return reverse_reachable_set

def justgetRR_LT(nodeV,outDict):
    reverse_reachable_set=set()
    activeSet=set()
    nodeSet=[nodeV]
    for node in nodeSet:
        activeSet.add(node)
        reverse_reachable_set.add(node)
    while activeSet.__len__()!=0:
        newActiveSet=set()
        if(log):
            print("当前激活的节点：",activeSet)
        for node in activeSet:
            neighbours=outDict.get(node,[])
            if(neighbours):
                activeNeighbor=random.sample(neighbours,1)[0]
                if(activeNeighbor.innode not in reverse_reachable_set):
                    newActiveSet.add(activeNeighbor.innode)
                else:
                    continue
        activeSet.clear()
        activeSet=newActiveSet
        if(log):
            print("生成的新激活节点:")
        reverse_reachable_set=reverse_reachable_set.union(newActiveSet)
    return reverse_reachable_set

if __name__ == '__main__':
    #if(log):
    time_start=time.time()
    imp()
    #if(log):
    time_end=time.time()
    if(log2):
        print("花费时间:",time_end-time_start)

