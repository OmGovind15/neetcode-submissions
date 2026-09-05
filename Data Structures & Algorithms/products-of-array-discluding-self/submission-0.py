class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        p=[1]*len(nums)
        i=len(nums)-1
        j=0
        l=1
        r=1
        while(i>=0):
            p[i]=r
            r=r*nums[i]
            i=i-1
        while(j<len(nums)):
            p[j]=p[j]*l
            l=l*nums[j]
            j=j+1
        return(p)
            
