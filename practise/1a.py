array = []
n = int (input("entre size of array : "))
for i in range (n):
  element=int(input(f"element{i+1}"))  
  array.append(element)
sum=0
for item in array:
  sum += item
print(sum)