from math import *

def specialPythagoreanTriplet(n):
 sumOfabc = n
 

 for i in range(n):
    a = i
    b = a
    c = n - a - b

    for j in range(n-a):
        #check if a<b<c
        if((c-j) < 0):
            break
        elif(a>b):
            continue
        elif((b+j)>=(c-j)):
            break
        elif(a == (b+j)):
            continue
        
        else:
            #check if a2+b2 = c2

            if(pow(a,2)+pow(b+j, 2) == pow(c-j, 2)):
                #print("{0} {1} {2} = {3}".format(a, b+j, c-j, a+ (b+j)+ (c-j)))
                sumOfabc = a* (b+j)* (c-j)


 return sumOfabc

print(specialPythagoreanTriplet(120))