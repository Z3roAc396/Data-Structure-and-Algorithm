price_array=[0,1,5,8,9,10,17,17,20,24,30]

def price(length):
    return price_array[length-1]

print(price(1))

def bottom_up_cut_rod(p,n):
    r=[None]*(n+1)
    r[0]=0
    for j in range(1,n+1):
        q=p[1]+r[j-1]
        for i in range(2,j+1):
            q=max(q, max(p[i]+r[j-i]))
        r[j]=q
    return q


