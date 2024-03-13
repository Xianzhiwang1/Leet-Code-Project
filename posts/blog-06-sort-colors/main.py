class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        We have a left pointer, a right pointer,
        and another pointer i
        """
        l,r = 0, len(nums) - 1
        i = 0

        def swap(i,j):
            # store the value at index i in tmp
            tmp = nums[i]
            # replace the value at index i with 
            # value at index j
            nums[i] = nums[j]
            nums[j] = tmp


        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l = l + 1
            elif nums[i] == 2:
                swap(i,r)
                r = r - 1
                i = i - 1
            i += 1

         

