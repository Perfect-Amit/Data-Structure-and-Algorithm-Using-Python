class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            mid = (l + r) // 2
            cnt = merge_sort(l, mid)
            cnt += merge_sort(mid + 1, r)
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - (mid + 1)
            temp = []
            i = l
            j = mid + 1
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= r:
                temp.append(nums[j])
                j += 1
            for i in range(l, r + 1):
                nums[i] = temp[i - l]
            return cnt
        return merge_sort(0, len(nums) - 1)