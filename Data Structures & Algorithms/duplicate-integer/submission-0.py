class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_new=set(nums)
        x=len(nums_new)
        if len(nums)>x:
            return True
        else:
            return False