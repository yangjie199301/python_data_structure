def solution(l1,l2):
    return (l1[0]*l2[1]-l1[1]*l2[0])/2

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
ans = 0
for i in range(len(l)-1):
    ans += solution(l[i],l[i+1])
print(int(ans))