class A:
    def show(self):
        print('A')

class B(A):
    def show(self):
        print('B')   


class C:
    def show(self):
        print('A')

class D(C):
    def show(self):
        print('B')   


class C(B, D):
   pass

print(C.mro())