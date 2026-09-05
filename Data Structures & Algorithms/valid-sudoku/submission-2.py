class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len_row=len_col=len(board[:][1])
        y=True
        
        def dup(a):
            x=False
            b=["1","2","3","4","5","6","7","8","9",'.']
            c=[0,0,0,0,0,0,0,0,0,0]
            for i in range(len(a)):
                if a[i] in b:
                    c[b.index(a[i])]=c[b.index(a[i])]+1
            
            for j in range(len(c)-1):
                if c[j]>1:
                    x=True
              
            return x
        
        def dup_sub(d):
            z=False
            b=["1","2","3","4","5","6","7","8","9",'.']
            c=[0,0,0,0,0,0,0,0,0,0]
            
            for i in range(3):
                for j in range(3):
                    if d[i][j] in b:
                        c[b.index(d[i][j])]=c[b.index(d[i][j])]+1
           
            for j in range(len(c)-1):
                if c[j]>1:
                    z=True
            return z

        for l in range(len_row):
            if dup(board[l][:])==True:
                y=False
        for m in range(len_col):
            col=[board[r][m] for r in range(len_row)]
            if dup(col)==True:
                y=False
        for i in range(0,len_row,3):
            for j in range(0,len_row,3):
                box=[]
                for k in range(i,i+3):
                    box.append(board[k][j:j+3])
                if dup_sub(box)==True:
                    y=False
        return y

