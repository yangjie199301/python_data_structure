from pythonds.basic.queue import Queue


def grenade(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        tmp = simqueue.dequeue()
        print("You catch a grenade: %s" % tmp)

    res = simqueue.dequeue()
    return "%s !!! You are the surviver" % res


print(grenade(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
