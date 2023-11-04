class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize the count of unique elements to 1 (the first element is always unique)
        unique_count = 1  
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # If the current element is different from the previous element, it's a unique element.
                # Update the unique element at the current position.
                nums[unique_count] = nums[i]
                unique_count += 1
        
        return unique_count
