def isPowerOfTwo(n):
    # Base case: if n is 1, it's a power of 2
    if n == 1:
        return True
    # Base case: if n is less than 1 or odd, it's not a power of 2
    elif n < 1 or n % 2 != 0:
        return False
    # Recursive case: continue dividing n by 2
    else:
        return isPowerOfTwo(n // 2)

# Example usage:
n = 16
print(isPowerOfTwo(n))
  # Output: True       
