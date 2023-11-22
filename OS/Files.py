import os
file_name = 'test.txt'

if os.path.exists(file_name):
    print(f"File {file_name} exist")
else:
    print(f"File {file_name} DOESNOT exist")

print(os.path.getmtime(file_name))

print('abspath', os.path.abspath(file_name))
print('relpath', os.path.relpath(file_name))