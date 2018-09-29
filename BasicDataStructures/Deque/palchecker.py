from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


def palchecker_list(aString):
    stillEqual = True
    if len(aString) < 2:
        return stillEqual
    else:
        first = 0
        last = len(aString)-1
        while last - first >1 and stillEqual:
            if aString[first] != aString[last]:
                stillEqual = False
                return stillEqual
            first += 1
            last -= 1
        return stillEqual


print(palchecker("lsdkjfskf"))
print(palchecker('radar'))

print(palchecker_list("lsdkjfskf"))
print(palchecker_list('radar'))