
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

    # Two Sum
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        i = 0 
        while i < len(nums):
            summand = nums[i]
            j = i+1
            while j < len(nums):
                if summand + nums[j] == target:
                    result.append(i)
                    result.append(j)
                j = j+1
            i = i+1
        return result
    
    # 28 find the index of the first occurrence in a string
    def strStrBAD(self, haystack: str, needle: str) -> int:
        result=0
        counter=0
        i = 0
        j = 0
        if len(needle) > len(haystack):
            return -1
        while counter < len(haystack):
            while j < len(haystack):
                if needle[i] == haystack[j]:
                    if i == (len(needle)-1):
                        result = j - len(needle) + 1
                        return result
                    i = i+1
                    j = j+1
            i = 0
            counter +=1
            j = counter
                    # if needle[i] == haystack[j]:
                    #     i=i+1
                    #     j=j+1
                    # else:
                    #     j = j+1
        return -1
    # 28 good solution O(n^2)
    def strStrGOOD(self, haystack: str, needle: str) -> int:
        if needle == "":
            return -1
        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) -1:
                    return i
        return -1





                
            



