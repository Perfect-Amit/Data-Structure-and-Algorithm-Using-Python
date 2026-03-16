class Solution:
    def getBiggestThree(self, grid):
        m=len(grid)
        n=len(grid[0])
        s=set()

        for i in range(m):
            for j in range(n):
                s.add(grid[i][j])
                k=1
                while i-k>=0 and i+k<m and j-k>=0 and j+k<n:
                    total=0

                    x=i-k
                    y=j

                    for t in range(k):
                        total+=grid[x+t][y+t]

                    for t in range(k):
                        total+=grid[x+k+t][y+k-t]

                    for t in range(k):
                        total+=grid[x+2*k-t][y-t]

                    for t in range(k):
                        total+=grid[x+k-t][y-k+t]

                    s.add(total)
                    k+=1

        res=sorted(s,reverse=True)
        return res[:3]