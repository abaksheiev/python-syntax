import Student as ms, pickle

studs = [
     ms.Student(10,'John', 'cs'),
     ms.Student(20,'Ajay', 'ec'),
     ms.Student(30,'Khan', 'me')]

with open('data/students.data', 'wb') as f:
    for s in studs:
        pickle.dump(s,f)
