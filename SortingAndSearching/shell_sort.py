def shell_sort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

        for startpostion in range(sublistcount):
            gap_insertion_sort(alist, startpostion, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount //= 2


def gap_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position= i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)
