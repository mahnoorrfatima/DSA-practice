class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) !=len(t):
        return False
      countS, countT={},{}
      for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)
      for c in countS:
        if countS[c] != countT.get(c,0):
          return False

      return True
          
#Time: O(n) 
# Space: O(n) 
#Remember: dictionary/hash-map lookup is O(1) average.







#My first solution that worked but hash map is preferred 
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
      if sorted(s)==sorted(t):
        return True
        
      return False

'''
#SORTING TAKES O(nlogn) time
#Hence, the better approach is O(n) using a hash map/dictionary.
