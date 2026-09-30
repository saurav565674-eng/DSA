num = int(input("enter no")) 
sum = 0
n= num
while (num > 0):
  sum = sum * 10 +(num % 10 )
  num//=10
print("palindrome",n==sum)