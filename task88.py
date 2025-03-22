from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arrow1 = 0
        arrow2 = 0
        while nums2:
            print(nums1[arrow1], nums2[arrow2], nums1)
            if nums1[arrow1] < nums2[arrow2] and nums1[arrow1] != 0:
                arrow1 += 1
                continue
            else:
                arrow1 += 1
                arrow2 += 1
                new_element = nums2.pop(0)
                nums1.insert(arrow1, new_element)

new_task = Solution()
new_task.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
