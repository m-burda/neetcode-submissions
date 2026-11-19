class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        two problems:
        1. find out which sequence nums[m] belongs to
        2. find out which of the two sequences the target should be in
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            # if we know that we have a contiguous sequence to the left
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    # the target cannot be in the left sequence
                    l = m + 1
                else:
                    r = m - 1
            # else we have a contiguous sequence to the right
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1