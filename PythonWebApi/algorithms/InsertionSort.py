import copy

def InsertionSort(Array):
    BigArray=[]
    BigArray.append(copy.deepcopy(Array))

    for i in range(len(Array)):
        key=Array[i]
        j=i-1
        while j>=0 and key<Array[j]:
            Array[j+1]=Array[j]
            BigArray.append(copy.deepcopy(Array))
            j-=1
        Array[j+1]=key
        BigArray.append(copy.deepcopy(Array))

    return BigArray
