array = []
item = int (input("entre size of array : "))
for i in range (item):
  element=int(input(f"element{i+1}"))  
  array.append(element)

num =int (input ("enter element "))
for index,item in enumerate(array):
  if item==num:
    print("no is at ",index)
