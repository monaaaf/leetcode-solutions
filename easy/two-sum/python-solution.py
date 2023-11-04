class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the values and their indices
        num_dict = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement (the number needed to reach the target)
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_dict:
                # If found, return the indices of the two numbers
                return [num_dict[complement], i]
            
            # Otherwise, store the current number and its index in the dictionary
            num_dict[num] = i
        
        # If no solution is found, return an empty list or raise an exception
        return []
