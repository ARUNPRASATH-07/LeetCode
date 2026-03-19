class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to reduce binary search steps
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # Number of elements in left partition
        
        # Binary search on the smaller array (nums1)
        low, high = 0, m
        while low <= high:
            # Partition position for nums1
            i = (low + high) // 2
            # Corresponding partition for nums2
            j = total_left - i
            
            # Handle boundaries for nums1
            nums1_left_max = float('-inf') if i == 0 else nums1[i-1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            # Handle boundaries for nums2
            nums2_left_max = float('-inf') if j == 0 else nums2[j-1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # Check if partition is correct
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Found the correct partition
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            elif nums1_left_max > nums2_right_min:
                # Too far right in nums1, move left
                high = i - 1
            else:
                # Too far left in nums1, move right
                low = i + 1