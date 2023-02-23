n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()
def search(start, end, item):
    while start<=end:
        mid = (start+end)//2
        if a[mid]==item:
            return True
        elif a[mid]<item:
            start=mid+1
        elif a[mid]>item:
            end=mid-1
    return False
for item in b:
    if search(0,len(a)-1,item):
        print(1)
    else:
        print(0)