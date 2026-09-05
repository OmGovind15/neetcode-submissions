class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i=0
        j=0
        nums=sorted(nums)
        while (j<len(nums)-1):
            t=1

            while( j<len(nums)-1 and nums[j+1]==nums[j]+1):
               
                t=t+1
                j=j+1
            
                
                #print(j)
                
            j=j+1
            
            if(t>i):
                i=t
                
           
        return i+1

            


            
            
            
