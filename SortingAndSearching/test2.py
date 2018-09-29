n = int(input())
l = list(map(int,input().split()))
tmp = ['0'] *7
print(tmp)
print(l)
for i in l:
    tmp[i-1] = str(i)
s = ''.join(tmp)
s = s.split('0')
res = []
for i in s:
    if len(i)<3:
        ans = ''
        for j in i:
            ans = ans + j + ' '
        res.append(ans)
    else:
        res.append(i[0]+'-'+i[-1]+' ')
r = ''.join(res)[:-1]
print(r)
