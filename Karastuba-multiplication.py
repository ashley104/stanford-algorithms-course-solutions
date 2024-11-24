def karatsuba(x, y):
    # Base case: if either x or y is a single-digit number
    if x < 10 or y < 10:
        return x * y
    
    # Determine the number of digits in the numbers
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2
    
    # Split the numbers into two halves
    xh = x // (10 ** n2)
    xl = x % (10 ** n2)
    yh = y // (10 ** n2)
    yl = y % (10 ** n2)
    
    # Recursively compute the three products needed for the algorithm
    s1 = karatsuba(xh, yh)
    s2 = karatsuba(xl, yl)
    s3 = karatsuba(xl + xh, yl + yh)
    s4 = s3 - s2 - s1
    
    # Combine the three products to get the final result
    return s1 * (10 ** (2 * n2)) + s4 * (10 ** n2) + s2

# Given 64-digit numbers
num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

# Compute the product using Karatsuba's algorithm
result = karatsuba(num1, num2)
print(result)