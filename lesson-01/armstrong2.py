def isArmstrong(n):
    if n < 0:
        return False
    digits = len(str(n))
    temp = n
    total = 0
    while temp > 0:
        digit = temp %10
        total += digit ** digits
        temp //= 10
    return total == n