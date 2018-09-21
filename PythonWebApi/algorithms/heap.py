import math

class heap:

    def __init__(self, array):
        self.heapsize=len(array)
        self.array=array
        self.build_max_heap()

    def parent(self,index):
        return math.floor((index-1)/2)
    def left(self,index):
        return index*2+1
    def right(self,index):
        return index*2+2
    def max_heapify(self, index):
        l=self.left(index)
        r=self.right(index)
        largest=index

        if l<self.heapsize and self.array[largest]<self.array[l]:
            largest=l
        if r<self.heapsize and self.array[largest]<self.array[r]:
            largest=r

        if largest!=index:
            self.array[largest], self.array[index]=self.array[index], self.array[largest]
            self.max_heapify(largest)

    def build_max_heap(self):
        length=self.heapsize
        for j in range(math.floor((length-1)/2), -1,-1):
            self.max_heapify(j)

    def heapsort(self):
        self.build_max_heap()
        length=self.heapsize
        for i in range(length-1,1,-1):
            self.array[0], self.array[i]=self.array[i], self.array[0]
            self.heapsize -=1
            self.max_heapify(0)

        self.heapsize=len(self.array)

    def maximum(self):
        return self.array[0]

    def extract_max(self):
        max=self.array[0]
        self.array[0]= self.array[self.heapsize-1]
        self.array.pop(-1)
        self.heapsize-=1
        self.max_heapify(0)
        return max

    def heap_increase_key(self, i, key):
        if key<self.array[i]:
            raise ValueError("Invalid Key")
        self.array[i]=key
        while i>0 and self.array[self.parent(i)]<self.array[i]:
            self.array[self.parent(i)], self.array[i]=self.array[i], self.array[self.parent(i)]
            i=self.parent(i)

    def max_heap_insert(self,key):
        self.heapsize +=1
        self.array.append(key)
        i=self.heapsize-1
        while i>0 and self.array[self.parent(i)]<self.array[i]:
            self.array[self.parent(i)], self.array[i]=self.array[i], self.array[self.parent(i)]
            i=self.parent(i)







