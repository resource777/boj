h,w,n,m = map(int,input().split())
tmp = 0
r,c=1,1
while tmp+n+1<h:
    tmp+=(n+1)
    r+=1
tmp = 0
while tmp+m+1<w:
    tmp+=(m+1)
    c+=1
print(r*c)
