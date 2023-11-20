from threading import *
from time import *

def display(str1):
    l.acquire() # start lock block
    for x in str1:
        print(x)
    l.release() # end lock block

l = Semaphore(1)
# l = Lock() the same syntax, just without number allowed thread

t1 = Thread(target=display, args=('HELLO WORLD',)) 
t2 = Thread(target=display, args=('12345 67890',)) 
t3 = Thread(target=display, args=('hello world',)) 

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()