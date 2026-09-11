class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        i=0
        j=len(numbers)-1
        while(i<len(numbers)//2 and j>=len(numbers)//2):
            if(numbers[i]+numbers[j]==target):
                a.append(i+1)
                a.append(j+1)
                numbers
            elif(numbers[i]+numbers[j]>target):
                j=j-1
            else:
                i=i+1
        
        
        return a

                    