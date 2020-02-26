from math import *
def powerDigitSum(exponent):
  result = pow(2, exponent)
  sum=0
  for i in str(result):
  	if i == '.':
  		break
  	sum += int(i)
  return sum
  

print(powerDigitSum(128))