
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
    
    def isPalindrome(self, x:int) -> bool:
        strx = str(x)
        inverted = strx[::-1]
        for i in range(len(strx)):
            if (strx[i] != inverted[i]):
                return False
        return True
    
    def isPalindromeII(self, x:int) -> bool:
        if x < 0:
            return False
        divider = 1
        while x >= divider*10:
            divider = divider*10
        while x:
            left = x // divider
            right = x % 10
            if (left != right):
                return False 
            # chop off the left digit
            x = x % divider
            # chop off the right digit
            x = x // 10
            # chop off two digits from divider
            divider = divider / 100
            # ready for the next iteration
        return True

    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return result
            result = result + strs[0][i]
        return result



                
            



