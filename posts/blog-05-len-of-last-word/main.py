
class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        i = 0
        result = 0
        s = s[::-1]
        space = True 
        while (i < len(s)) and space:
            if s[i] != " ":
                result = result + 1
                i = i+1
            else:
                if result == 0:
                    i = i+1
                else:
                    space = False
        return result
                
            



