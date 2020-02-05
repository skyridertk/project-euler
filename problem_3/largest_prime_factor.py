def largestPrimeFactor(value):
  max_val = 0
  prime = 2

  while value>1:
    
    if value % prime == 0:
      value /= prime
      max_val = prime
      
    else:
      
      while True:
        is_prime = True
        prime += 1
        if prime % 2 == 0:
            is_prime = False
        
          
        if is_prime == True:
          break
      

  
  return max_val

print(largestPrimeFactor(600851475143))
