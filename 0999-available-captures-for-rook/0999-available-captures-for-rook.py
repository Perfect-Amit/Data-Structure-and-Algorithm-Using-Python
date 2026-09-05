class Solution:
    def numRookCaptures(self,board:list[list[str]])->int:
        for i in range(8):
            for j in range(8):
                if board[i][j]=='R':
                    r,c=i,j
        ans=0
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for dr,dc in directions:
            i,j=r+dr,c+dc
            while 0<=i<8 and 0<=j<8:
                if board[i][j]=='B':
                    break
                if board[i][j]=='p':
                    ans+=1
                    break
                i+=dr
                j+=dc
        return ans