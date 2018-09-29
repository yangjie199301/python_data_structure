from pythonds.basic.stack import Stack

def divideByBase(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base

    ans = ''
    while not remstack.isEmpty():
        ans += digits[remstack.pop()]
    return ans

print(divideByBase(25,2))
print(divideByBase(26,26))