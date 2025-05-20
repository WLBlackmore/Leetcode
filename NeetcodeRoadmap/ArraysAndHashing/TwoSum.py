# Easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # target - number -> index
        goal = {}
        
        for index, number in enumerate(nums):
            
            if number in goal:
                return [goal[number], index]
            
            else:
                goal[target - number] = index
                
# Time: O(n)
# Space: O(n)       
            
            
   