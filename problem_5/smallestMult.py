def smallestMult(n):
  value = 2
  escape = False
  while not escape:
    
    escape = True
    for i in range(n, 1, -1):
   
      if value%i != 0:
        escape = False
        break
    
    value += 2
    
  return value-2

print(smallestMult(20))
