class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        shortArr = nums1 if len(nums2) > len(nums1) else nums2
        longArr = nums2 if len(nums2) > len(nums1) else nums1
        longDict = {}
        intersections = []
        for i, num in enumerate(longArr):
            if num in longDict:
                longDict[num] += 1
            else:
                longDict[num] = 1
        for num in shortArr:
            if num in longDict and longDict[num] > 0:
                intersections.append(num)
                longDict[num] -= 1
        return intersections