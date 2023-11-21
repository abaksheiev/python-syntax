import sqlite3

conn = sqlite3.connect('univ.db')

cur =conn.cursor()

#cur.execute('create table Dept(Deptno integer primary key, name text)')
#cur.execute('create table Student(roll integer primary key , name text , city text ,deptno integer , foreign key (deptno) references Dept(deptno))')

conn.commit()

cur.close()

conn.close()