data = "hello world"
print(data)

data="Don't you konw \"Python\"?"
print(data)

a="Hello"
b="World"
print(a+' '+b)
a="String"
print(a*3)

a=(1,2,3,4)
print(a)

data=dict()
data['Apple']="apple"
data['Banana']="banana"
data['Coconut']="coconut"

print(data)
if 'Apple' in data:
    print("exist")
key_list=data.keys()
key_value=data.values()
key_item=data.items()

print(key_list)
print(key_value)
print(key_item)

data=set([1,1,2,3,4,4,5])
print(data)

a=set([1,2,3,4,5])
b=set([3,4,5,6,7])

print(a&b)
print(a|b)
print(a-b)

"""
n=int(input())
data=list(map(int, input().split()))
print(data)
"""

import sys
data=sys.stdin.readline().rstrip()
