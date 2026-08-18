#Sorting  takes O(n log n) - the problem explicitly says the solution must be O(n).

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

      num_set = set(nums)
      longest = 0 

      for num in num_set:

        #Beginning of a sequence or no
        if num - 1 not in num_set:
          
          length = 1

          #Keep looking for the next number
          while num + length in num_set:
            length += 1 

          longest = max(longest, length)

      return longest 

#Complexities:
#Time Complexity: O(n)
#Space: O(n) 
