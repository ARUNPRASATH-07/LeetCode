class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store numbers and their indices
        num_map = {}
        
        # Iterate through the list with index and value
        for i, num in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_map:
                # If found, return the stored index and current index
                return [num_map[complement], i]
            
            # Store the current number and its index in the dictionary
            num_map[num] = i
        
        # Since the problem guarantees one solution, this line may not be reached
        return []