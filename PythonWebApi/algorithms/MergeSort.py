import math

def Merge(Array,p,q,r):
    n1=q-p+1
    n2=r-q
    Array1=Array[p:q+1].copy()
    Array2=Array[q+1:r+1].copy()

    index1=0
    index2=0
    index3=p

    while(index1<n1 and index2<n2):

        if(Array1[index1]<=Array2[index2]):
            Array[index3]=Array1[index1]
            index1+=1
            index3+=1
        else:
            Array[index3] = Array2[index2]
            index2 += 1
            index3 += 1

    while(index1<n1):
        Array[index3]=Array1[index1]
        index1+=1
        index3+=1

    while(index2<n2):
        Array[index3]=Array2[index2]
        index2 += 1
        index3 += 1

def MergeSortR(Array,l,r):

    if l<r:
        m=math.floor((l+r)/2)
        MergeSortR(Array,l,m)
        print('a')
        print(l,m)
        MergeSortR(Array,m+1,r)
        print('b')
        print(m+1,r)
        Merge(Array,l,m,r)

def MergeSort(Array):
    print(len(Array)-1)
    MergeSortR(Array,0,len(Array)-1)


Array=[1,3,5,7,2,10]
MergeSort(Array)
print(Array)



