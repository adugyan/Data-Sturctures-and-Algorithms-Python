#The basics of an array, the data structure that organizes items sequentially
strings = ['a', 'b', 'c', 'd']

print(strings[3])

strings.append('e') # O(1)adds an object to an end of the list

strings.pop() # O(1) deletes from the end of the list
strings.pop()

#adds as the new first, has to loop through
strings.insert(0, 'x') #O(n)

#inserts at index 2. Splice
strings.insert(2,'alien') #O(n)

print(strings)

