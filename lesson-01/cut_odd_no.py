def countOddDigits(n):
    count = 0
    n=abs(n)
    if n==0:
        return 0
    while n>0:
        digit = n%10
        if digit %2 !=0:
            count +=1
        n //= 10
    return count