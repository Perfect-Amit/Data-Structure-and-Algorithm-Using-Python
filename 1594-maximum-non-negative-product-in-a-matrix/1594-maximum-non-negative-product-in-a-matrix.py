class Solution:
    def maxProductPath(self, grid):
        m=len(grid)
        n=len(grid[0])
        
        max_dp=[[0]*n for _ in range(m)]
        min_dp=[[0]*n for _ in range(m)]
        
        max_dp[0][0]=grid[0][0]
        min_dp[0][0]=grid[0][0]
        
        for i in range(1,m):
            max_dp[i][0]=max_dp[i-1][0]*grid[i][0]
            min_dp[i][0]=min_dp[i-1][0]*grid[i][0]
        
        for j in range(1,n):
            max_dp[0][j]=max_dp[0][j-1]*grid[0][j]
            min_dp[0][j]=min_dp[0][j-1]*grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                val=grid[i][j]
                
                a=max_dp[i-1][j]*val
                b=min_dp[i-1][j]*val
                c=max_dp[i][j-1]*val
                d=min_dp[i][j-1]*val
                
                max_dp[i][j]=max(a,b,c,d)
                min_dp[i][j]=min(a,b,c,d)
        
        res=max_dp[m-1][n-1]
        
        if res<0:
            return -1
        
        return res%(10**9+7)