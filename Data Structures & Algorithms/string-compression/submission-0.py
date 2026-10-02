class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = 0
        character = ''
        sol = ""
        for c in chars:
            if character == '':
                character = c
                curr += 1
            elif character == c:
                curr += 1
            else:
                sol += character
                if curr > 1:
                    sol += str(curr)
                character = c
                curr = 1
    
        sol += character
        if curr > 1:
            sol += str(curr)
    
        for i in range(len(sol)):
            chars[i] = sol[i]
            
        return len(sol)