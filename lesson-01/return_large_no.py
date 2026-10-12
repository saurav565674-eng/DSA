def returnLargestDigit(n):
    n = abs(n)
    largest = 0
    while n >0:
        digit = n % 10
        if digit>largest:
            largest = digit
        n //= 10
    return largest