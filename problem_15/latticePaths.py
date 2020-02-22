from math import factorial as fac
#xCy = x! / (y! (x-y)!)
def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom


def latticePaths(gridSize):
  
  return binomial(2*gridSize, gridSize)


print(latticePaths(9))