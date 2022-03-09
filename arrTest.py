#선택정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

#삽입정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1],arr[j]
        else:
            break
print(arr)

#quick search
data=[5,7,9,0,3,1,6,2,4,8]
#data=[5,4,9,0,3,1,6,2,7,8]
def quick_sort(data, start, end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<= end and data[left] <= data[pivot]:
            left +=1
        while right > start and data[right] >=data[pivot]:
            right -=1

        if left>right: #엇갈렸다면 작은 데이터와 피벗을 교체
            data[right], data[pivot]=data[pivot],data[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            data[left], data[right]=data[right],data[left]

    quick_sort(data, start,right-1)
    quick_sort(data, right+1, end)

quick_sort(data, 0, len(data)-1)
print(data)

print("=======quick sort 1============================")
#파이썬의 장점을 살린 퀵 정렬 소스
data=[5,7,9,0,3,1,6,2,4,8]
def quick_sort1(data):
    if len(data) <=1:
        return data

    pivot=data[0] #pivot
    tail=data[1:] #pivot을 제외

    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]

    return quick_sort1(left_side)+[pivot]+quick_sort1(right_side)

print(quick_sort1(data))

