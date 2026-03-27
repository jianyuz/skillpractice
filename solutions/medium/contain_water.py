#11 contain most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # if between i, j hold most water
        # (j-i ) * min(hi,hj) = 49
        #from outer siade and shrink?
        # move the shorter one among the two
        # greedy
        
        if height is None or len(height) == 1:
            return 0

        i = 0
        j = len(height) -1

        max_water = 0
        while i < j:
            cur_water = (j-i) * min(height[i], height[j])
            if cur_water > max_water:
                max_water = cur_water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
