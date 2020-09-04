#Splits and string and then prints it alphatically

fh = "But soft what light through yonder window breaks It is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief"

lst = []
words = fh.split()
words.sort()

for line in range (len(words)):
  #word = words[line]
  lst.append(words[line])

print(lst)
