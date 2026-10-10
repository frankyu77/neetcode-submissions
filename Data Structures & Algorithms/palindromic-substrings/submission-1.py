class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
            
            # even
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
        return count
