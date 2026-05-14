class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, s, path):
            if not node:
                return
            s += node.val
            path.append(node.val)
            if not node.left and not node.right:
                if s == targetSum:
                    res.append(path[:])
            dfs(node.left, s, path)
            dfs(node.right, s, path)
            path.pop()
        dfs(root, 0, [])
        return res