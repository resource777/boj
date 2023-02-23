x,y = map(int,input().split())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
val=0
for i in range(x):
    val+=days[i]
val+=y
val-=1
print(day[val%7])
