#everytime we see a new name add a number to counts
'''make an empty dictionary and make a list with values. Loop through the list, use the iterative variable as the key. '''

counts = dict()
names = ['zhen', 'Kennedy', 'Power', 'Denji', 'Denji']

for name in names:
  if name not in counts:
    counts[name] = 1
  else:
    counts[name] = counts[name] + 1 
print(counts)

''' 
counts = dict()
names = ['zhen', 'Kennedy', 'Power', 'Denji', 'Denji']

for name in names:
  counts[name] = counts.get(name, 0) + 1
print(counts)
'''
