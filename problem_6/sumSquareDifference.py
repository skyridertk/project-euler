from math import *

def sumSquareDifference(n):
  sum_values = pow(n*(n+1)/2, 2)

  sum_squares_values = n*(n+1)*(2*n+1)/6

  return sum_values - sum_squares_values


print(sumSquareDifference(100))