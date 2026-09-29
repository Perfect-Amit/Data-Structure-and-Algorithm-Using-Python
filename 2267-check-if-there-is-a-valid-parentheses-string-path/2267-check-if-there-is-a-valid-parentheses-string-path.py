class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]==')' or grid[m-1][n-1]=='(':
            return False
        dp=[[set() for _ in range(n)] for _ in range(m)]
        dp[0][0]={1}
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                current=1 if grid[i][j]=='(' else -1
                balances=set()
                if i>0:
                    for balance in dp[i-1][j]:
                        new_balance=balance+current
                        if new_balance>=0:
                            balances.add(new_balance)
                if j>0:
                    for balance in dp[i][j-1]:
                        new_balance=balance+current
                        if new_balance>=0:
                            balances.add(new_balance)
                dp[i][j]=balances
        return 0 in dp[m-1][n-1]