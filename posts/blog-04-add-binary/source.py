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

    # LeetCode 88 Merge Sorted Array
    def merge(self, nums1: list[int], m: int, nums2: list[int], n:int) -> None:
        '''
        return nums1 in-place.
        '''
        # obtain last index
        last = m + n -1
        # index goes from zero to n-1
        m = m-1
        n = n-1
        # now we merge with pointers start at the last index
        while (m >= 0) and (n >= 0):
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m = m-1
            else:
                nums1[last] = nums2[n]
                n = n-1
            last = last - 1
        while (n>=0):
            nums1[last] = nums2[n]
            last = last - 1
            n = n - 1
        
    # LeetCode 69 Sqrt(x)
    def mySqrt(self, x: int) -> int:
        i = 1
        while x>= i**2:
            i = i+1
        return i-1

    # 35 Search Insert Position
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        while (i < len(nums)):
            if nums[i] == target:
                return i
            else:
                i = i+1
        
        i = 0
        while (i < len(nums)):
            if nums[i] < target:
                i = i+1
            else:
                return i
        return i

    # want log(n) runtime 
    def searchInsertII(self, nums: list[int], target: int) -> int:
        # left pointer
        l = 0
        # right pointer
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid -1
        return l






