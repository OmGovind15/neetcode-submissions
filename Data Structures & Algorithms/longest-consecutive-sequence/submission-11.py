class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums=sorted(nums)
        def uni(x):
            z=[]
            y=set(x)
            for i in y:
                z.append(i)
            return z
        nums=uni(nums)
        t=1
        i=0
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1
        for j in range(len(nums)-1):
            #print (i)
            if nums[j+1]==nums[j]+1:
                t=t+1
                #print(t)
                #print(i)
                if(t>i):
                    i=t
                    
            else:
                
                if(t>i):
                    i=t
                    t=1
                else:
                    t=1

        return i

        

            


            
            
            
