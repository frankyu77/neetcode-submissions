'''
You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.
    - s1, s2, s3 are lowercase characters

Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met
- |n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
- s = s1 + s2 + ... + sn
- s = s1 + s2 + ... + sn
- Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...


Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"
n = ["aa", "aa"]
m = ["bbbb"]
"aabbbbaa"
"bbbbaaaa"

n = [a, a, a, a]
n = [aa, aa]
n = [aaa, a]
n = [a, aaa]
n = [aaaa]

m = [b, b, b, b]
m = [bb, bb]
m = [bbb, b]
m = [b, bbb]
m = [bbbb]


aaaa
a aaa
a a aa
a a a a
aaa a
aa a a
aa aa
a aa a
2^n possible substrings for s1 and s2


1. get all possible subtrings of s1 and s2 --> how???
    - susbtrings1 = []
    - substrings2 = []

    - 

2. for each substring i in substrings1:
    - compare that with every susbtring j in substring2
    - if abs(len(substrings1[i]) - len(substrings2[j])) <= 1:
        - interleave the substrings: 2 ways
        - check if s3 == any of those 2 ways
            return True 
    return False

------------------------------------------------------------------

Input: s1 = "aaaa", s2 = "bbbb", s3 = "caabbbbaa"
                                          |
caaaa
|

cbbbb
|

i = pointer for s1
j = pointer for s2
k = i+j pointer for s3

if s1[i] == s3[k]:
    - i = i+1
    - recurse for next index --> check that also True for the rest
if s2[j] == s3[k]:
    - j = j+1
    - recruse for next index --> check that also True for the rest
'''
from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def sameString_from_and(i: int, j: int) -> bool:
            if i >= len(s1) and j >= len(s2):
                return True

            k = i + j

            if i < len(s1) and s1[i] == s3[k] and sameString_from_and(i+1, j):
                return True
            if j < len(s2) and s2[j] == s3[k] and sameString_from_and(i, j+1):
                return True
            
            return False
        return sameString_from_and(0, 0)



        