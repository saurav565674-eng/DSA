class Solution:
    def digitCounts(self, n: int) -> int:
        if  n == 0:
            return 1
        count=0
        n=abs(n)
        while n>0:
            count+=1
            n//=10
        return count