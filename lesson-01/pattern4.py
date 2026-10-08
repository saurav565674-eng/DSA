#center pattern
n=int(input("enter :"))
for i in range(1,n+1):
  print("  "*((n+1)-i),end="")
  print(" *  "*i)

#center pattern with alternate symbol
n=int(input("enter :"))
for i in range(1,n+1):
  print("  "*((n+1)-i),end="")
  print(" *  "*i) if i%2==0 else print(" $  "*i)

#print the pattern
n=3
for i in range(1,n+1):
  print("*"*i)
