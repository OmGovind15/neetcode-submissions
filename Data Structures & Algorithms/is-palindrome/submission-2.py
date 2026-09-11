class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        #print(s)
        p=[]
        for i in s:
            if i.isalnum():
                p.append(i)
        print(p)
        x=0
        y=len(p)-1
        r=False
        if len(p)%2!=0:
            c=0
            while(x<len(p)//2 and y>len(p)//2):

                #print('x',x)
                
                #print('y',y)
                #print('value_X',p[x])
                #print('value_Y',p[y])

                if(p[x]==p[y]):
                    c=c+1
                    print('xx',x)
                    print('yy',y)
                    print('cc',c)
                x=x+1
                y=y-1
            if(c==len(p)//2):
                r=True
            print('c',c)
        m=0
        n=len(p)-1
        if len(p)%2==0:
            d=0
            while(m<len(p)//2 and n>=len(p)//2):
                print('m',x)
                print('n',y)
                if(p[m]==p[n]):
                    d=d+1
                m=m+1
                n=n-1
            #print('d',d)
            if(d==len(p)//2):
                r=True
        return r


