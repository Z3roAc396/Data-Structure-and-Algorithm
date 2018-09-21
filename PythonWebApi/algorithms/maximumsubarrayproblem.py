import math

def find_max_crossing_subarray(Array,low,mid,high):
    left_sum=Array[mid]
    sum=Array[mid]
    max_left=mid
    for i in range(mid-1,low-1,-1):
        sum+=Array[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i

    right_sum = Array[mid]
    sum = Array[mid+1]
    max_right=mid+1
    for j in range(mid+2, high+1):
        sum += Array[j]
        if sum > left_sum:
            right_sum = sum
            max_right= j

    return (max_left,max_right,left_sum+right_sum)

def find_maximum_subarray(Array,low,high):
    if low==high:
        return (low, high, Array[low])
    else:
        mid=math.floor((high+low)/2)
        (left_low,left_high,left_sum)=find_maximum_subarray(Array,low,mid)
        (right_low,right_high,right_sum)=find_maximum_subarray(Array,mid+1,high)
        (cross_low, cross_high, cross_sum)=find_max_crossing_subarray(Array, low,mid,high)
        if left_sum>right_sum and left_sum>cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>cross_sum and right_sum>left_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
