class Binheap():
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self,k):
        self.append(k)
        self.current_size = self.current_size + 1
        self.per_up(self.current_size)

    def delmin(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.per_down(1)
        return retval

    def per_up(self, i):
        while i // 2 >0:
            if self.heap_list[i] < self.heap_list[i//2]:
                tmp = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def per_down(self,i):
        while (i*2) <= self.current_size
            mc = self.minChild(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1

    def bulid_heap(self,alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.per_down(i)
            i = i - 1