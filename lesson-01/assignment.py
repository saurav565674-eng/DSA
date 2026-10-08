#print sum of first 10 even no
# sum = 0
# for i in range (1,11,2):
#   sum += i
# print(sum)

#accept 2 values s and n .print square of first n nostarting from s
# s= int(input("enter no"))
# n= int(input("enter no"))
# for i in range(s,n+s):
#   print(i*i)

#accept sentence from user and count the vowels(easy)
# n = str(input("enter sentence"))
# vowels="aeiou"
# count=0
# for i ,ch in enumerate(n):
#   if ch in vowels or ch in vowels.upper():
#     count+=1
# print(count)

#accept sentence from user and count the vowels(medium)
n = str(input("enter sentence"))
vowels="aeiou"
repeat={}
count=0
for i ,ch in enumerate(n):
  if ch in vowels or ch in vowels.upper():
    count+=1
    if ch in repeat:
      repeat[ch]

print(count)
print(repeat)

#remove duplicate from list
# li=[5,5,4,6,84,7,7]
# unique=[]
# for i in li:
#   if i not in unique:
#     unique.append(i)
#   print(unique)






