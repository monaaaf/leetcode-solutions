class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize the count of non-val elements
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                # If the current element is not equal to val, move it to the position k
                nums[k] = nums[i]
                k += 1
                
        return k
