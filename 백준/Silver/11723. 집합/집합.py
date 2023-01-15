import sys
m = int(sys.stdin.readline())
st = 0
for i in range(m):
    inst = sys.stdin.readline().split()
    if inst[0] == 'add':
        st |= 1<<int(inst[1])
    elif inst[0] == 'remove':
        st &= ~(1<<int(inst[1]))
    elif inst[0] == 'check':
        if st & (1<<int(inst[1])):
            print(1)
        else:
            print(0)
    elif inst[0] == 'toggle':
        st ^= 1<<int(inst[1])
    elif inst[0] == 'all':
        st = (1<<21) - 1 
    elif inst[0] == 'empty':
        st = 0
