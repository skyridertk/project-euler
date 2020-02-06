from math import *

def largestPalindromeProduct(n):
    lower_limit = int(pow(10, n-1))
    upper_limit = int(lower_limit * 10) - 1
    max_result = 0

    while upper_limit>=pow(10, n-1):
        

        for i in range(upper_limit+1, lower_limit-1, -1):

            product = upper_limit * i
            
            if(product < max_result):
                break
            
            
            res = product == reverse(product)
            
            if(res and product > max_result):
                max_result = product
        
            
        upper_limit -= 1
        
    return max_result

def reverse(num): 
    return int(num != 0) and ((num % 10) * (10**int(log(num, 10))) + reverse(num // 10))

print(largestPalindromeProduct(3))