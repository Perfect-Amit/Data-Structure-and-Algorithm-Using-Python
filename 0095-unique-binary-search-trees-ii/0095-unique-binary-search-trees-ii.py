class Solution:
    def generateTrees(self, n):
        if n==0:
            return []

        def build(start,end):
            res=[]
            if start>end:
                res.append(None)
                return res

            for i in range(start,end+1):
                left=build(start,i-1)
                right=build(i+1,end)

                for l in left:
                    for r in right:
                        node=TreeNode(i)
                        node.left=l
                        node.right=r
                        res.append(node)

            return res

        return build(1,n)