import multiprocessing
import os

def square(n):
    import psutil
    import random

    cpu_id = random.choice([0,1])

    p = psutil.Process()
    p.cpu_affinity([cpu_id])
    print("current processor id:", os.sched_getaffinity(os.getpid()))
    return(n*n)

if __name__ == '__main__':
    mylist = [1,2,3,4]

    p = multiprocessing.Pool()
    result = p.map(square,mylist)

    p.close()

    print(result)