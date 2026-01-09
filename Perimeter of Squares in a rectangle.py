def perimeter(n):
    a = 1
    b = 1
    output = 0
    for i in range(0,n + 1):  
        currenta = a
        a = b  
        b = currenta + b  
        output += currenta
        
    return 4 * output

print(perimeter(5))