cnt = int(input())
numbers = sorted(list(map(int,input().split())))
if cnt == 1:
    print(numbers[0]*numbers[0])
else:
    print(numbers[0]*numbers[-1])