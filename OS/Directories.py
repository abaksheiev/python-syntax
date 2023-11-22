import os

print(f'name: {os.name}')

print(f'getlogin: {os.getlogin()}')

#print(f'getcwd: {os.getcwd()}')
#print(f'chdir: ./', os.chdir('../../'))
#print(f'getcwd: {os.getcwd()}')

print(f'listdir: {os.listdir()}')

print('Create \'TestFolder\' folder ',os.mkdir('TestFolder'))

print(f'listdir: {os.listdir()}')

print('Delete \'TestFolder\' folder ',os.rmdir('TestFolder'))

print(f'listdir: {os.listdir()}')