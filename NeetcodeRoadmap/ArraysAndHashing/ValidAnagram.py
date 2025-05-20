# Easy
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False
        
        occS = {}
        occT = {}
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            occS[s_char] = occS.get(s_char, 0) + 1
            occT[t_char] = occT.get(t_char, 0) + 1
            
        return occS == occT

# Time: O(n)
# Space: O(n)