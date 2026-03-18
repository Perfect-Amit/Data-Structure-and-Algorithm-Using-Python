class Solution:
    def buildTree(self, preorder, inorder):
        mp={v:i for i,v in enumerate(inorder)}
        self.pre=0

        def build(l,r):
            if l>r:
                return None

            root_val=preorder[self.pre]
            self.pre+=1

            root=TreeNode(root_val)
            mid=mp[root_val]

            root.left=build(l,mid-1)
            root.right=build(mid+1,r)

            return root

        return build(0,len(inorder)-1)