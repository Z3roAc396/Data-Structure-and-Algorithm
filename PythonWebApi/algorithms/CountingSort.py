def CountingSort(Array,k):

    count=[0]*(k+1)
    B=[None]*len(Array)
    for x in range(len(Array)):
        count[Array[x]]+=1

    for x in range(1,len(count)):
        count[x]=count[x]+count[x-1]



    for j in range(len(Array)-1,-1,-1):
        B[count[Array[j]]-1]=Array[j]
        count[Array[j]]-=1

    for x in range(len(Array)):
        Array[x]=B[x]

Array=[0,2,4,8,7,8]
CountingSort(Array,8)
print(Array)