class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collections = set()
        for operations, i in enumerate(range(len(nums)-1,-1,-1), start=1):
            if nums[i]<=k:
                collections.add(nums[i])
            if len(collections)==k:
                 return operations
