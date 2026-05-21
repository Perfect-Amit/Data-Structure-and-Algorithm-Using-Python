class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jumpings = set(stones)
        last_stone = stones[-1]
        memo = {}
        def solve(current_stone, prev_jump):
            if current_stone == last_stone:
                return True
            if (current_stone, prev_jump) in memo:
                return memo[(current_stone, prev_jump)]
            for jump in [prev_jump - 1, prev_jump, prev_jump + 1]:
                if jump > 0:
                    next_stone = current_stone + jump
                    if next_stone in jumpings:
                        if solve(next_stone, jump):
                            memo[(current_stone, prev_jump)] = True
                            return True
            memo[(current_stone, prev_jump)] = False
            return False
        return solve(0, 0)