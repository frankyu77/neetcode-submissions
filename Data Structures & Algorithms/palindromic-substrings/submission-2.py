class Solution:
    def countSubstrings(self, s: str) -> int:
        rsf = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            curr = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                curr += 1
                l -= 1
                r += 1
            rsf += curr

            # even
            l, r = i, i+1
            curr = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                curr += 1
                l -= 1
                r += 1
            rsf += curr
        return rsf