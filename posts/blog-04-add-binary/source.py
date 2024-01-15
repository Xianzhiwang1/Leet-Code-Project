class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) -1
        j = len(b) -1
        sum = 0
        carry = 0
        digit = 0
        soln = ""
        # we use or in our while loop since the two numbers can have different length
        while i >= 0 or j >= 0:
            sum = carry
            if (i >= 0):
                sum += int(a[i])
            if (j >= 0):
                sum += int(b[j])
            # print("sum is", sum)
            digit = sum % 2
            # soln stores our answer, we first compute the 2^0 th digit, then 2^1 th digit ...
            soln = str(digit) + soln
            # print("soln is", soln)
            carry = sum // 2
            i = i -1
            j = j -1
        # after we exit the while loop, we need to take care of the last carry term
        if (carry != 0):
            soln = "1" + soln 
        return soln




