from pythonds.basic.stack import Stack



def toStr(n, base):
    convertString = '0123456789ABCDEF'
    ans = ''
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n % base]


print(toStr(1453,16))



rStack = Stack()


def toStr2(n, base):
    convertString = '0123456789ABCDEF'
    while n > 0 :
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])
        n = n // base
    res = ''
    while not rStack.isEmpty():
        res = res + str(rStack.pop())

    return res

print(toStr2(1453,16))