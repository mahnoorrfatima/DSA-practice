class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present=set()

        for num in nums:
            if num in present:
                return True
            present.add(num)

        return False 


# Time: O(n) -  single pass, and each set lookup/insert is O(1) on average.
# Space: O(n) - worst case every element is unique and ends up in the set.

#1-minute revision
#When you see it: "any duplicates?" / "seen before?" → reach for a set.
