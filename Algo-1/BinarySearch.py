from typing import List


class Solution:
    def binary_search(nums: List[int], target: int) -> int:
        """
            A binary search is best (properly) used on an already sorted list.
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if(nums[middle] == target):
                return middle
            if target < middle:
                right = middle - 1
            else:
                left = middle + 1
        return -1


print(Solution.binary_search([1, 3, 5, 8, 12], 8))