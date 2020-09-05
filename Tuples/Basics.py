d = dict(ein=3, awei=22)
#print(sorted(d.items()) for one instance
oByKeys = []
oByValues = []

for (k,v) in d.items():
  oByKeys.append((k,v))
  oByValues.append((v,k))

print(sorted(oByKeys))
print('--------------')
print(sorted(oByValues))
print('--------------')
print(sorted(oByKeys, reverse=True))
print('--------------')
print(sorted(oByValues, reverse=True))
#O(n)

'''
print('Order by keys: ')
for (k,v) in sorted(d.items()):
  print (k,v)
print('--------------')

print('Order by values: ')
for (k,v) in sorted(d.items()):
  print(v, k)
print('--------------')

print('Descending Order(values): ')
for (k, v) in sorted(d.items(), reverse=True):
  print (v, k)
print('--------------')

print('Descending Order(Keys): ')
for (k, v) in sorted(d.items(), reverse=True):
  print (k, v)
print('Finished')
''' 
