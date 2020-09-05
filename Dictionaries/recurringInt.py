'''
1. Create an empty dictionary
2. loop through the list
3. Use the iterative variable with the empty dictionary and the get method to increment
4. If a value count == 2, print the double
n) '''
lsts = [2,5,1,2,3,5,1,2,4]
wrong = [2,4,6,3]

def findDouble(arrs):
  repeats = dict()
  for arr in arrs:
    repeats[arr] = repeats.get(arr, 0) + 1
    if repeats[arr] == 2: 
      print(arr)
      break
    else:
      continue
      print('Not Defined')
  
    
    

findDouble(lsts)

#0(n)
