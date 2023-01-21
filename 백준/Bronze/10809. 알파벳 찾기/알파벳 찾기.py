lst=['-1']*26
s = input()
for i in range(len(s)):
    if lst[ord(s[i])-ord('a')]=='-1':
        lst[ord(s[i])-ord('a')]=str(i)
print(' '.join(lst))