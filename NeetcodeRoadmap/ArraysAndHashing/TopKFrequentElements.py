# Medium
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occ = {}
        
        for num in nums:
            occ[num] = occ.get(num, 0) + 1 
        
        sorted_keys = sorted(occ.keys(), key=lambda c: occ[c], reverse=True)
        
        topK = sorted_keys[:k]
        
        return topK

# Time: O(nlgn)
# Space O(n)
# Not Optimal