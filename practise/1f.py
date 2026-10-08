array =[]
n=int(input("enter no"))
for i in range (n):
  element = int (input(f"enter element {i+1}"))
  array.append(element)
unique=[]
for item in array:
  if item is not unique:
    unique.append(item)
    
print(unique)