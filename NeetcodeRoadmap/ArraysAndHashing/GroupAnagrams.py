# Medium
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # abdc freq -> list
        anaGroups = {}
        
        for word in strs:
            alphaKey = [0] * 26
            
            for char in word:
                alphaKey[ord(char) - ord('a')] = alphaKey[ord(char) - ord('a')] + 1
            
            if tuple(alphaKey) in anaGroups:
                anaGroups[tuple(alphaKey)].append(word)
            
            else: 
                anaGroups[tuple(alphaKey)] = [word]
                
        
        return anaGroups.values()   

# Time: O(n * m)
# Space O(m)