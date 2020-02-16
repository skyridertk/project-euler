def divisibleTriangleNumber(n):
  counter =1
  triangle_num = 1
  while True:
    if(numberOfDivisors(triangle_num) >= n):
      break
    
    counter+= 1
    triangle_num += counter

    

  
  return triangle_num

def numberOfDivisors(value):
  divisors = 0
  if value == 1:
    return 1
  else:
    for i in range(1, value+1):
      if value % i == 0:
        divisors += 1
    return divisors

print(divisibleTriangleNumber(167))