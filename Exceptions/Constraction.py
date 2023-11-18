L = [10, 20, 30, 40, 50]

try:
    index = int(input('Enter index: '))
    print(L[index])
except IndexError as msg:
    print('Invalid index: ', msg)
except ValueError  as msg:
    print('Engter only interger value: ', msg)
finally:
  print("The 'try except' is finished")

