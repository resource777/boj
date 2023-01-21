n = int(input())
for _ in range(n):
    val=1
    total=0
    is_previous_o = False
    for i in input():
        if i=='O':
            total+=val
            val+=1
            is_previous_o=True
        else:
            val=1
            is_previous_o=False
    print(total)
