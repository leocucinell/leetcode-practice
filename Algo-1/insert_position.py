from typing import List


def insert_pos(nums: List[int], target: int):
    """
        Search list for num, if num not there, return index where it should be
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if(nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return right + 1

print(insert_pos([1, 4, 7, 13, 20, 25], 9))