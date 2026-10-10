"""
You are given an encoded string s, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. There will not be input like 3a, 2[4], a[a] or a[2].

The test cases are generated so that the length of the output will never exceed 100,000.


Input: s = "2[a3[b]]c"

2 * recurse(a3[b])
a + recurse(3[b])
3 * recurse(b)

Output: "abbbabbbc"

stack = [2a, 3b]
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == "[":
                stack.append((curr, num))
                curr, num = "", 0
            elif ch == "]":
                prev, k = stack.pop()
                curr = prev + k * curr
            else:
                curr += ch
        return curr
            