n=int(input())
base_data=list(map(int, input().split()))
s=int(input())
search_data=list(map(int, input().split()))

def binary_search(data, target, start, end):
    if start>end:
        return None
    mid=int((start+end)/2)
    if data[mid]==target:
        return mid
    elif data[mid]<target:
        start=mid+1
    elif data[mid]>target:
        end=mid-1
    return binary_search(data, target, start, end)

base_data.sort()


for i in search_data:
    if binary_search(base_data, i, 0, n-1)==None:
        print('no', end=' ')
    else:
        print("yes", end=" ")
