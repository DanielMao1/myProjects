import  random


class my_max_heap():
#
# for i in range(10):
#     print(i)
    def init(self,nodeList):
        self.maxheap=[[] for _ in range(0,len(nodeList)+1)]
        self.next_empty=1#index所在元素为空
        idx = len(self.maxheap)-1
        self.next_empty=len(self.maxheap)
        for item in nodeList:
            self.maxheap[idx] +=[item]
            self.roor_shift_donw(idx)
            idx -= 1
    def add(self,newItem):
        self.maxheap+=[newItem]
        currentIndex =self.next_empty
        self.next_empty+=1
        while currentIndex>1:
            if(self.maxheap[currentIndex]>self.maxheap[int(currentIndex/2)]):
                self.maxheap[currentIndex],self.maxheap[int(currentIndex/2)]=self.maxheap[int(currentIndex/2)],self.maxheap[currentIndex]
                currentIndex=int(currentIndex/2)


    def remove(self):
        if(self.next_empty>1):
            self.next_empty-=1
            rt=self.maxheap[1]
            self.maxheap[1]=self.maxheap[self.next_empty]
            self.roor_shift_donw(1)
            return rt
        else:
            return None

    def roor_shift_donw(self,parentNode):
        while True:
            left_node_index = 2 * parentNode
            if left_node_index >= self.next_empty:
                return
            right_node_index = 2 * parentNode + 1
            if right_node_index >= self.next_empty:
                max_idx = left_node_index
            else:
                if self.maxheap[left_node_index][0] > self.maxheap[right_node_index][0]:
                    max_idx = left_node_index
                else:
                    max_idx = right_node_index

            if self.maxheap[parentNode][0]>= self.maxheap[max_idx][0]:
                return

            self.maxheap[parentNode], self.maxheap[max_idx] = self.maxheap[max_idx], self.maxheap[parentNode]

            parentNode = max_idx

