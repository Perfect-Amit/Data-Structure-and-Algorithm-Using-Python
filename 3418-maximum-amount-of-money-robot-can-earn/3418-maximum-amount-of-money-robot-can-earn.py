class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m=len(coins)
        n=len(coins[0])
        dp=[[[-float('inf')]*3 for _ in range(n)] for _ in range(m)]
        dp[0][0][0]=coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1]=0
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i==0 and j==0:
                        continue
                    val=coins[i][j]
                    for pi,pj in [(i-1,j),(i,j-1)]:
                        if pi>=0 and pj>=0:
                            dp[i][j][k]=max(dp[i][j][k], dp[pi][pj][k]+val)
                            if val<0 and k>0:
                                dp[i][j][k]=max(dp[i][j][k],
                                                dp[pi][pj][k-1])
        return max(dp[m-1][n-1])