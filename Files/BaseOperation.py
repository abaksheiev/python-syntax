file = open('data/MyData.txt','a')
str1 = file.writelines('test line\n')
print(str1)
file.close()