import Student as ms, pickle

with open('data/students.data','rb') as f:
    for i in range(3):
        s = pickle.load(f) 
        s.display()
        print('-- --')