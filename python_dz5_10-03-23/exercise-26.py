def pow(a, b):
    if b == 1:
        return a * 1
    elif b == 0:
        return 1
    else:
        b -= 1
    
    return a * pow(a, b)

print(pow(3, 5))