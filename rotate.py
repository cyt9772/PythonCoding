
def rotate_90(a):
    row=len(a)
    col=len(a[0])

    result=[[0]*row for _ in range(col)]
    for r in range(col):
        for c in range(row):
            result[c][row-1-r]=a[r][c]

    return result

data=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(rotate_90(data))
