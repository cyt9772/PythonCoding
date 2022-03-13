
def sequencial_search(data, target):
    for i in range(len(data)):
        if target==data[i]:
            return i+1
        else:
            continue

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
""" sequential search    
input_data=input().split()
n=int(input_data[0])
target=input_data[1]

data=list(input().split())

print(sequencial_search(data,target))
"""
""" 
binary search
"""
n,target=map(int, input().split())
data=list(map(int, input().split()))

print(binary_search(data, target, 0, len(data)))

