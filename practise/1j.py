class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels='aeiou'
        max_v =0
        max_c =0
        for ch in set(s):
            count =s.count(ch)
            if ch in vowels :
                max_v=max(max_v,count)
            else :
                max_c =max(max_c,count)
        return max_v + max_c