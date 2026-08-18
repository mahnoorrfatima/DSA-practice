class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      output= [1] * len(nums)

      #Left products
      prefix=1

      for i in range(len(nums)):
        output[i]=prefix
        prefix *= nums[i]

      #Right products
      postfix=1

      for i in range(len(nums) - 1, -1, -1):
        output[i] *=postfix
        postfix *= nums[i]

      return output


#Time complexity: O(n) 
#Space complexity: 0(1) 
