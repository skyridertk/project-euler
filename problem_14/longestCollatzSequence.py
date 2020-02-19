def longestCollatzSequence(limit):
  occurrence = 0
  num = 0

  for i in range(2, limit+1):
    temp = 0
    numbr = i
    while numbr>1:
      temp+=1
    
      if(numbr%2 == 0):
        numbr = numbr/2
      else:
        numbr = 3*numbr + 1

    if(temp>=occurrence):
      occurrence=temp
      num = i


  return num


print(longestCollatzSequence(5847))
