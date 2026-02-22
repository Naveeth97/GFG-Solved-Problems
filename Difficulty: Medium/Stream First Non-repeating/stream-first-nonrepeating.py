from collections import deque
class Solution:
    def firstNonRepeating(self, s):
        # code here
        
        
        freq = [0] * 26
        d = deque()
        
        result = ""
        
        for ch in s:
            
            freq[ord(ch) - ord('a')] += 1
            d.append(ch)
            
            while d and freq[ord(d[0]) - ord('a')] > 1:
                
                d.popleft()
                
            if d:
                result += d[0]
            else:
                result += "#"
                
        return result