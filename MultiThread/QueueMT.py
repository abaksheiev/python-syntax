from queue import *
from threading import *
from time import *

q = Queue()
q.empty()
def producer(que):
    i = 1
    while True:
        que.put(i)
        print('Proudcee', i)
        i += 1
        sleep

def consumer(que):
    while True:
        x = que.get()
        print('Consumer:', x)
        
t1 = Thread(target=lambda:producer(q))
t2 = Thread(target=lambda:consumer(q))

t1.start()
t2.start()

t1.join()
t2.join()