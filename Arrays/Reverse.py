#Create a function the reverses a string
#uses rnage(start, stop, step) 

#start	Optional. An integer number specifying at which position to start. Default is 0
#stop	Required. An integer number specifying at which position to stop (not included).
#step	Optional. An integer number specifying the incrementation. Default is 1

def reverse(stri):
  mylist=[]
  #starts at the last index, ends
  for i in range(len(stri)-1,0,-1):
    mylist.append(stri[i])
  #puts a space in between the indices and makes it readable
  return ''.join(mylist)

try:
  x=reverse('Hi my name is Kofi')
  print(x) 
 
#It can be improved to take more than one argument
except TypeError: 
  print('TypeError, only takes 1 positional argument')
