class Solution:
    def longestRepeating(self, s: str, queryCharacters: List[str],
                         queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a
            lc, rc, p, su, best, length = a
            lc2, rc2, p2, su2, best2, length2 = b
            same = rc == lc2
            new_p = p
            new_su = su2
            new_best = max(best, best2)
            if same:
                new_best = max(new_best, su + p2)
                if p == length:
                    new_p = length + p2

                if su2 == length2:
                    new_su = length2 + su
            return (
                lc,
                rc2,
                new_p,
                new_su,
                new_best,
                length + length2
            )
        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        build(1, 0, n - 1)
        ans = []
        for i, ch in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, i, ch)
            ans.append(tree[1][4])
        return ans