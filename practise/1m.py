def reverseArray(arr):
    if isinstance(arr,dict):
        arr=arr.get("arr",[])
    left=0
    right= len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr