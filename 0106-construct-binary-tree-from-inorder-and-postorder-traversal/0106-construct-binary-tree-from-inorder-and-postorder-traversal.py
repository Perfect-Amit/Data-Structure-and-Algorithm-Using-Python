class Solution:
    def buildTree(self, inorder, postorder):
        mp={v:i for i,v in enumerate(inorder)}
        self.post=len(postorder)-1

        def build(l,r):
            if l>r:
                return None

            root_val=postorder[self.post]
            self.post-=1

            root=TreeNode(root_val)
            mid=mp[root_val]

            root.right=build(mid+1,r)
            root.left=build(l,mid-1)

            return root

        return build(0,len(inorder)-1)