class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     while k > 0:
    #         num = nums.pop()
    #         nums.insert(0, num)
    #         k -= 1

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     rot = -(k % len(nums))
    #     nums2 = nums[rot:] + nums[:rot]
    #     for i in range(len(nums)):
    #         nums[i] = nums2[i]

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     k %= n

    #     start = count = 0
    #     while count < n:
    #         current, prev = start, nums[start]
    #         while True:
    #             next_idx = (current + k) % n
    #             nums[next_idx], prev = prev, nums[next_idx]
    #             current = next_idx
    #             count += 1

    #             if start == current:
    #                 break
    #         start += 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1