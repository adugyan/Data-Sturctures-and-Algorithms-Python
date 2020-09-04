'''
1.Make an empty dictionary
2. Use split() to turn the string into a list and store
3. loop through the list. Use itervative variable as Key
4. use dictionary and key with get method to count instances.
'''
fh = "But soft what light through yonder window breaks It is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief"

count = dict()
words = fh.split()

for word in words:
  count[word] = count.get(word, 0) + 1
print(count)
