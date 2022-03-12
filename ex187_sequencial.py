
def sequencial_search(data, target):
    for i in range(len(data)):
        if target==data[i]:
            return i+1
        else:
            continue


input_data=input().split()
n=int(input_data[0])
target=input_data[1]

data=list(input().split())

print(sequencial_search(data,target))

