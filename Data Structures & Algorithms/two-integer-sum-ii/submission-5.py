class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        i=0
        j=1
        while(i<len(numbers)-1):
            #print("i",i)
            if(j>len(numbers)-1):
                i=i+1
                j=i+1
            if(j<=len(numbers)-1):
                if(numbers[i]+numbers[j]==target):
                    a.append(i+1)
                    a.append(j+1)
                    i=len(numbers)
                else:
                    j=j+1
        
        return a

                    