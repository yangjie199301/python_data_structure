def listsum(numlist):
    if len(numlist) < 2:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])



l = [1,2,3,4,5,6,7,8,9,10]
print(listsum(l))