class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        shortArr = nums1 if len(nums2) > len(nums1) else nums2
        longArr = nums2 if len(nums2) > len(nums1) else nums1
        shortDict = {}
        for i, num in enumerate(shortArr):
            if num in shortDict:
                shortDict[num].append(i)
            else:
                shortDict[num] = [i]
        
