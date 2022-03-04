from itertools import permutations,combinations, product, combinations_with_replacement

result=sorted([('홍길동', 50), ('이순신', 70), ('아무개', 90)], key=lambda x:x[1], reverse=True)
print(result)

data=['A','B','C']
result=list(permutations(data,3))
print(result)
result=list(permutations(data,2))
print(result)

data=['a','b','c']
result=list(combinations(data,2))
print(result)
result=list(product(data,repeat=2))
print(result)



