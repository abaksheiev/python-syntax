from threading import *
from time import *

class Alpabets(Thread):
    # predefined name of method
    def run(self):
        for i in range(65, 91):
            print(chr(i))

t = Alpabets()
t.start()
for i in range(65,91):
    print(i)
t.join()