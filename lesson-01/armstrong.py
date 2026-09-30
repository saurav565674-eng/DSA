sum = 0

num = 125 
p = len (str(num))
n = num 
while num > 0:
  sum += (num %10)**p
  num //=10
print(n==sum,"it armstrong:")
