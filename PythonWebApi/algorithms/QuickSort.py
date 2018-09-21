def QuickSort(Array,p,r):
    if p<r:
        q=Partition(Array,p,r)
        QuickSort(Array,p,q-1)
        QuickSort(Array,q+1,r)


def Partition(Array,p,r):
    pivot=Array[r]
    i=p-1

    for j in range(p,r):
        if Array[j]<=pivot:
            i=i+1
            Array[j],Array[i]=Array[i],Array[j]

    Array[i+1],Array[r]=Array[r],Array[i+1]
    return i+1



