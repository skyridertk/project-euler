def fiboEvenSum(n):
  a1, a2 = 1, 2

  my_sum = a2

  for i in range(2, n):
      print(i)
      temp = a2
      a2 = a1+a2
      a1 = temp

      lastdigit = int(repr(a2)[-1])
      
      if(lastdigit % 2 == 0):
          my_sum += a2
    
      
  return my_sum


print(fiboEvenSum(4000000))
