import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum():
    lst = []

    n = int(input('Enter the number of elements: '))
    for i in range (0,n):
      ele = int(input())
      lst.append(ele)
    print(lst)
    print(sum(lst))

simpleArraySum()
