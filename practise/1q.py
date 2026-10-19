def highestOccurringElement(nums):
    freq ={}
    for num in nums:
        freq [num]= freq.get(num,0)+1
    maxf = max(freq.values())
    candidates =[]
    for num ,count in freq.items():
        if count==maxf:
            candidates.append(num)
    return min (candidates)