def selection_sort(alist):
    for fillslots in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslots+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslots]
        alist[fillslots] = alist[positionOfMax]
        alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)