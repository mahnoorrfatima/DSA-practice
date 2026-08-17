class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagrams={}

      for s in strs:
        key="".join(sorted(s))

        if key not in anagrams:
          anagrams[key]= []

        anagrams[key].append(s) 

      return list(anagrams.values())

#TIME COMPLEXITIES 
#sorting: O(k log k)
#sorting for n strings: n x O(k log k) = 0(n. k log k) 

#SPACE
#O(n . k)  = O(nk) 


