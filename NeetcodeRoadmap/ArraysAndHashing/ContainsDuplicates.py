# Easy
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
# Time: O(n)
# Space: O(n)