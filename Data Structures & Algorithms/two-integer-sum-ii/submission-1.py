class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        for i in range(len(numbers)-1):
            for j in (numbers[i+1:len(numbers)]):
                if(numbers[i]+j==target):
                    a.append(i+1)
                    a.append(numbers.index(j)+1)
        return a

                    