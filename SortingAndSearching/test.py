n = int(input())
def solution(n):
    if n ==1:
        return str(2)
    elif n ==2:
        return str(3)
    else:
        if n%2==0:
            return str(3)+solution((n-2)//2)
        else:
            return str(2)+solution((n-1)//2)
print(solution(n)[::-1])