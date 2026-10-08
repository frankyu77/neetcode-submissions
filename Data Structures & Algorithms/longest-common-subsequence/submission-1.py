from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def commonStringOf_and(i: int, j: int) -> int:
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + commonStringOf_and(i+1, j+1)
            
            skip1 = commonStringOf_and(i+1, j)
            skip2 = commonStringOf_and(i, j+1)

            return max(skip1, skip2)
        
        return commonStringOf_and(0, 0)
