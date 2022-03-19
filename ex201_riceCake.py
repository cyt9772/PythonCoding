n, target=map(int, input().split())
data=list(map(int, input().split()))

#sort data
data.sort()


def binSearch(data, target, start, end):
    if start>=end:
        return
    mid=(start+end)//2
    result=sum([x-mid for x in data if x>=mid])

    if result==target:
        return mid
    elif result>target:
        start=mid+1
    elif result<target:
        end=mid-1

    return binSearch(data, target, start, end)

print(binSearch(data, target, 0, max(data)))