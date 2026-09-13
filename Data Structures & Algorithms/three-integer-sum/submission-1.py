class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        i=0
        nums=sorted(nums)
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                if(nums[i]+nums[l]+nums[r]==0):
                    #print(("1"))
                    #print([nums[i],nums[l],nums[r]])
                    a.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r=r-1
                    if(nums[l]==nums[l-1]):
                        l=l+1
                    if(nums[r]==nums[r+1]):
                        r=r-1
                elif(nums[i]+nums[l]+nums[r]<0):
                    #print("2")
                    l=l+1
                else:
                    #print("3")
                    r=r-1
        return a


                
                
                    

            

                    

