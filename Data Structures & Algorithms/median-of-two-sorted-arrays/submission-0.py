class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        with a naive O(m + n) time and O(m+n) space solution, we would build out a new array out of given arrays using two pointers and return the median
        """

        merged = []
        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1

        if p1 < len(nums1):
            merged.extend(nums1[p1:])
        
        if p2 < len(nums2):
            merged.extend(nums2[p2:])

        mid = len(merged) // 2
        if len(merged) % 2:
            return merged[mid]
        else:
            return (merged[mid - 1] + merged[mid]) / 2
