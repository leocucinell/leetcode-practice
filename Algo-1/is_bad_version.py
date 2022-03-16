class Solution:
    def is_bad_version(num):
        #Made for testing purposes
        if num == 5:
            return True
        return False

    def first_bad_version(self, n: int) -> int:
        """
            Use a binary search to determine the first bad version
        """
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if(self.is_bad_version(mid)and not self.is_bad_version(mid-1)):
                return mid
            if(self.is_bad_version(mid)):
                right = mid - 1
            else:
                left = mid + 1
        return -1

print(Solution.first_bad_version(Solution, 20))
