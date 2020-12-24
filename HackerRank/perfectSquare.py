import math 
def is_square(n):
    if n < 0:
      print(f"{n} is negative and cannot be square")
      return False
    else:
      sqrRoot = math.sqrt(n)
    
    check = sqrRoot.is_integer()
    print(check)
    if check == False:
        print(f"{n} is not a perfect square")
        return False # fix me
    else:
        print(f"{n} is a perfect square")
        return True

is_square(2)
