array = []
item = int (input("entre size of array : "))
for i in range (item):
  element=int(input(f"element{i+1}"))  
  array.append(element)

lg =array[0]
sm=array[0]
for item in array:
  if item> lg:
    lg = item
  if item<sm:
    sm = item

slg =array[0]
ssm=array[0]
for item in array:
  if item <slg and item> lg:
    slg = item
  if item >ssm and item<sm:
    sm = item
print(lg)
print(sm)
print("second",slg)
print("ssm",ssm)