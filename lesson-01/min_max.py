arr = [100, 363, 53, 26, 28, 45, 75]
minimum = maximum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print(minimum)  
print(maximum)  