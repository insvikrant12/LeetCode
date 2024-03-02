class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res= [0] * n
        left= 0
        right= n-1
        for k in range(n):
                if abs(nums[left])>abs(nums[right]):
                    res[n-1-k]=abs(nums[left])**2
                    left += 1
                else:
                    res[n-1-k]=abs(nums[right])**2
                    right-=1
        return res
