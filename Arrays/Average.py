#With a for function

def makeList():
  values = []
  #n = int(input())
  for i in range(4): #or n for user input
    newValue = float(input())
    values.append(newValue)
  print(float(sum(values)/len(values)))

makeList()
  
#With a while function 
def getAverage():
  values = []
  print("Enter Integers. When you're finished enter 'done' and the program will calculate the average")
  while True:
    n = (input())
    if n == "done": break
    nums = float(n)
    values.append(nums)
  
  print(sum(values)/len(values))
      
getAverage()
