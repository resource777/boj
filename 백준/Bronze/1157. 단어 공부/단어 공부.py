s = input().upper()
alpha = [0]*26
for c in s:
    alpha[ord(c)-ord('A')]+=1
if alpha.count(max(alpha))>=2:
    print('?')
else:
    print(chr(alpha.index(max(alpha))+ord('A')))
