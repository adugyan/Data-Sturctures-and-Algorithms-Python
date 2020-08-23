import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

if N % 2 == 0 and N in range(2, 5):
  print('{0} is not weird'.format(N))
elif N % 2 == 0 and N in range(6, 20):
  print('{0} is weird'.format(N))
elif N % 2 == 0 and N > 20:
  print('{0} is not weird'.format(N))
else:
  print('{0} is weird'.format(N))
