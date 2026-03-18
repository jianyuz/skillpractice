class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #two pointers
        #front pointer find the element equal to val
        #back pointer find the element not equal to val
        #swap them
        #until two pointers equal
        #how to count elements not qual to val. depends on 
        # the value of nums[i]

        i = 0
        j = len(nums) -1
        
        while i < j :
            while nums[i] != val and i < j:
                i += 1
            print(f"1st i={i} j={j}")
            while nums[j] == val and i < j:
                j -= 1

            print(f"2nd i={i} j={j}")
            # swap
            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        
        if i == j:
            if nums[i] == val:
                return i
            else:
                return i+1
