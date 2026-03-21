def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        str_len = len(s)
        max_len = 0
        for i in range(str_len):
            part_max = self.partial_max_len(s, i)
            if part_max > max_len:
                max_len = part_max
        
        return max_len
    
    def partial_max_len (self, s:str, i:int) -> int:
        start = end = i
        seen = set(s[start])
        str_len = len(s)
        max_len = 0
        while end < str_len -1:
            end += 1
            if s[end] in seen:
                cur_len = end - start 
                if  cur_len > max_len:
                    max_len = cur_len
                start = end
                seen.clear()
            seen.add(s[end])
        
        cur_len = end - start + 1
        if cur_len > max_len:
            max_len = cur_len
        return max_len


def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        #max running substring without repeating is 26
        #for each position in Str
        #grab maximumly 26 char.
        #check for duplicate among the 26

        max_len = 1
        #upper case, lower case + digits
        for i in range(len(s)):
            end = min(i + 256, len(s))
            sub_str = s[i: end]
            part_max = self.part_max_len(sub_str)
            if part_max > max_len:
                max_len = part_max
        return max_len
    
    def part_max_len(self, sub_str: str) -> int:
        seen = set()
        max_len = 0
        for c in sub_str:
            if c in seen:
                return max_len
            else:
                max_len += 1
            seen.add(c)
        return max_len
def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = j = 0
        #sliding window
        #grow right until see duplicate
        #shrink left until over the duplicate
        seen = set(s[0])
        max_len = 1
        while j < len(s) -1:
            j += 1
            if s[j] in seen:
                if max_len < j -i:
                    max_len = j - i
                while i < j and s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                i += 1
            seen.add(s[j])
        
        if max_len < j -i +1:
            max_len = j - i +1
        
        return max_len

class Solution: #best
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = j = 0
        #sliding window
        #grow right until see duplicate
        #shrink left until over the duplicate
        seen = set()
        max_len = 1
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_len = max(max_len, j-i +1)
            j += 1
        return max_len
        


