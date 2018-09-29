def binarySearch(alist, item):
    first = 0
    last = len(alist) -1
    found = False

    while first <= last and not found:
        midpoint = (first + last) //2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint + 1
    return found


def binarySearchRc(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearchRc(alist[:midpoint], item)
            else:
                return binarySearchRc(alist[midpoint+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
print(binarySearchRc(testlist, 3))
print(binarySearchRc(testlist, 13))