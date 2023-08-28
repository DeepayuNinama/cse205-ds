def PowerOfFour(n):

    if (n==1):
        return True
    
    if (n <= 0 or n % 4 == 1):
        return False

    else:
        return PowerOfFour(n // 4)

n = 16
print(PowerOfFour(n))     