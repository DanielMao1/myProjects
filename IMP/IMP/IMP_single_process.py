import numpy as np
import random
import time
import argparse
import multiprocessing as mp
import sys
import math
from memory_profiler import profile
sum=0
core=8
log=False
log2=False

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
    return nodenum,outDict,nodenum,edgenum
#@profile
def nodeSelection_revise(setR,k,nodeNum):

    skset=list()
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
            skset.append(max_node)
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
                    skset.append(nextNode)
                    break

    return skset

def node_selection_revise2(rrsets, k):
    global root_idx

    skset = []

    nodeToRRmap = {}
    sid = 0
    for rrset in rrsets:
        for vid in rrset:
            if vid not in nodeToRRmap:
                nodeToRRmap[vid] = [sid]
            else:
                nodeToRRmap[vid].append(sid)
        sid += 1

    root_idx = len(nodeToRRmap) + 1
    maxheap = [[] for nothing in range(root_idx)]
    def maintain(i):
        while True:
            left_idx = 2 * i
            if left_idx >= root_idx:
                return
            right_idx = 2 * i + 1
            if right_idx >= root_idx:
                max_idx = left_idx
            else:
                if maxheap[left_idx][1] > maxheap[right_idx][1]:
                    max_idx = left_idx
                else:
                    max_idx = right_idx

            if maxheap[i][1] >= maxheap[max_idx][1]:
                return

            maxheap[i], maxheap[max_idx] = maxheap[max_idx], maxheap[i]

            i = max_idx

    idx = len(maxheap) - 1
    for vid, sid_lst in nodeToRRmap.items():
        score = len(sid_lst)
        maxheap[idx] += [vid, score, sid_lst]
        maintain(idx)
        idx -= 1

    seedNum = 0
    seedCovered = set()
    while seedNum < k:
        maxNode = maxheap[1]
        seedNext = list(filter(lambda e: e not in seedCovered, maxNode[2]))
        maxNode[1], maxNode[2] = len(seedNext), seedNext

        if maxheap[1][1] >= max(maxheap[2][1], maxheap[3][1]):
            vid, _, sid_lst = maxheap[1]

            root_idx -= 1
            maxheap[1] = maxheap[root_idx]
            maintain(1)

            skset.append(vid)
            seedNum += 1

            for sid in sid_lst:
                seedCovered.add(sid)
        else:
            maintain(1)

    return skset

#@profile
def imp():
    time_start=time.time()
    if(log2):
        print("time_start:",time_start)
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
    nodes, outDict, nodenum, edgenum=initReverseGraph(graphPath)



    if(log):
        print("生成可达集开始...")
    setR=getRRs(nodes,outDict,model,time_limit*1/2)
    time_end=time.time()
    if(log):
        print("生成的集合数量：",len(setR))
    if(log2):
        print("生成的集合数量：",len(setR))
        print("time_end：",time_end)
        print("生成集合所花时间：",time_end-time_start)
    time_nodeselection_start=time.time()

    #setSk=nodeSelection_revise(setR,seedNum,nodes)
    setSk=node_selection_revise2(rrsets=setR,k=seedNum)
    time_nodeselection_end = time.time()
    if(log2):
        print("node selection time:",time_nodeselection_end-time_nodeselection_start)
    for node in setSk:
        print(node)
    sys.stdout.flush()

    # 3.S∗k= NodeSelection(R, k);
    # 4.return S∗
#@profile
def getRRs(nodeNum,outDict,model,time_limit):
    RRunitsize=0
    loopTime=0
    loopPeriod=16
    totalSize=0
    setRsize=0
    setR=[]
    totalTime=0
    loopNum=0
    space_limit=1024*1024*1024
    get_rr_function=None
    if (model == 'IC'):
        get_rr_function=justgetRR_IC
    else:
        get_rr_function=justgetRR_LT
    while totalTime<=time_limit and totalSize<=space_limit:
        if(log):
            loopNum+=1
            print("第%d次循环开始"%(loopNum))
        timeStart=time.time()
        nodeV=random.randint(1,nodeNum)
        if(log):
            print("生成 %d 号节点的可达集"%(nodeV))
        currentReachableSet=get_rr_function(nodeV,outDict)
        timeEnd=time.time()
        totalTime+=timeEnd-timeStart
        if(loopTime==0):
            RRunitsize=sys.getsizeof(currentReachableSet)
            totalSize-=setRsize
            setRsize=sys.getsizeof(setR)
            totalSize+=setRsize
        loopTime+=1
        loopTime%=16
        totalSize+=RRunitsize
        setR.append(currentReachableSet)
        if(log):
            print("花费时间:",totalTime)
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


    time_start=time.time()
    imp()
    time_end=time.time()
    if(log2):
        print("花费时间:",time_end-time_start)

