from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for key, val in enumerate(nums):
            if (target - val) in hashtable:
                return [key, hashtable[target - val]]
            hashtable[val] = key

res = Solution()
print(res.twoSum([3, 2, 4], 6))

