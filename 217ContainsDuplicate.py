#217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_mark=set()
        for i in len(nums):
          if i in set_mark:
            return True
          set_mark.add(i)
        return False
