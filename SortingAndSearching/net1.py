h1,m1,s1 = list(map(int,input().split(':')))
h2,m2,s2 = list(map(int,input().split(':')))


def f1(h,m,s):
    return float((30*h)+(0.5*m)+(1/120*s))


def f2(h,m,s):
    return float((360*h)+(6*m)+(0.1*s))


def f3(h,m,s):
    return float((21600*h)+(360*m)+(6*s))


print(int(f1(h2,m2,s2)-f1(h1,m1,s1)))
print(int(f2(h2,m2,s2)-f2(h1,m1,s1)))
print(int(f3(h2,m2,s2)-f3(h1,m1,s1)))
