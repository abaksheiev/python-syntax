kmInMile = 1.6

miles2km = lambda miles: kmInMile * miles

add = lambda a, b : a + b

greatest = lambda a, b: a if a > b else b


print('Kms', miles2km(10))

print('Add', add(5,7))

print('greater', greatest(7,5))
