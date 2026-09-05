class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        set_one=set(s)
        set_two=set(t)
        def count(x,y):
            sum=0
            for j in range(len(x)):
                if y==x[j]:
                    sum=sum +1
            return sum

        if set_one==set_two:
            c=0
            for i in set_one:
                if count(s,i)==count(t,i):
                    c=c+1
            if c==len(set_one):
                return True    
            else:
                return False
        else:
            return False

                