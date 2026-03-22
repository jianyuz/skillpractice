class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        l_len = len(nums) 
        if l_len == 0:
            return 0
        r = l_len -1

        while l < r and l >=0 and r < l_len:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = min(r, mid + 1)
            else:
                r = max(l, mid - 1)
        
        if l == r and nums[l] == target:
            return l
        elif l == r and nums[l] < target:
            return l+1 #position +1
        elif l == r and nums[l] > target:
            return max(0, l) #take its position
        print(f"{l}, {r}")

        
