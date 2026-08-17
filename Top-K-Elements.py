class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      count = {}
      for num in nums:
        count[num]=count.get(num,0) + 1

      #Buckets
      buckets = [[] for _ in range(len(nums) + 1)]


      #Frequency bucket 
      for num, freq in count.items():
        buckets[freq].append(num)

      result=[]

      for freq in range(len(buckets) - 1,0,-1):
        for num in bucckets[freq]:
          result.append(num)

          if len(result) == k:
            return result 

#Complexity:
#Time:  O(n)
#Space: O(n) 
