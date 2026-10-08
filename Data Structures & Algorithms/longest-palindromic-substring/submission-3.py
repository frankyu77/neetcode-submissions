'''
Given a string s, return the longest substring of s that is a palindrome.
- contains digits and letters
- can either remove a char from the from or from the back
- want the longest substring
    - if multiple same length can return any

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.


Input: s = "ababd"
- check if string itself is palindrom
- Decision: if curr is not valid palindrom: 
    - remove first char, remove last char
        - remove first:
            - check if string[1:] is valid
        - remove last:
            - check if string[:-1] is valid
    - if curr is valid:
        return
'''
from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def longest_from_to(i: int, j: int) -> str:
            if i >= j:
                return (i, j)
            if s[i] == s[j]:
                a, b = longest_from_to(i+1, j-1)
                if b - a == (j - 1) - (i + 1):
                    return (i, j)
            
            a1, b1 = longest_from_to(i+1, j)
            a2, b2 = longest_from_to(i, j-1)

            return (a1, b1) if b1 - a1 >= b2 - a2 else (a2, b2)
        i, j = longest_from_to(0, len(s) - 1)
        return s[i : j + 1]






