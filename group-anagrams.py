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

#ANOTHER APPROACH (better actually):
class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list) # if key does not exist, this would create a default key with that value --> empty list instead of an error

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] +=1  #  # 'a' -> index 0, 'b' -> index 1

            result[tuple(count)].append(s)

        return list(result.values()) 



