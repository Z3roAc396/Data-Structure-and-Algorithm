def RandomizedSelect(A,p,r,i):
    if p==r:
        return A[r]
    q=Randomized_Partition(A,p,r)
    k=q-p+1
    if k==i:
        return A[q]
    elif i<k:
        return RandomizedSelect(A,p,q-1,i)
    else:
        return RandomizedSelect(A,q+1,r,i-k)

def Randomized_Partition(A,p,r):
    pivot=Array[r]
    i=p-1

    for j in range(p,r):
        if A[j]<=pivot:
            i=i+1
            A[j],A[i]=A[i],A[j]

    A[i+1], A[r]= A[r], A[i+1]

    return i+1