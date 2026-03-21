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
  
