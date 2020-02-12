def primeSummation(n):
  sumOfPrime = 0
  start = 1
  
  while start < n:
    start = findNextPrime(start)
    if(start < n):
      sumOfPrime += start
    else:
      break

    
  
  return sumOfPrime


def findNextPrime(number):
    number += 1
    
    while True:
        is_prime = True

        if((number % 2 == 0 or number % 3 == 0) and number >3):
            is_prime = False
            number += 1
        else:

            for i in range (2, number):
                if number % i == 0:
                    number += 1
                    is_prime = False
                    break
            
        if is_prime:
            break

    return number

print(primeSummation(2001))
