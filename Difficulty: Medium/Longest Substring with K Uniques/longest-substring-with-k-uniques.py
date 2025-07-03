class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        dic = {}
        
        n = len(s)
        
        left = 0
        
        right = 0
        max_length = -1
        
        while right < n:
            
            if s[right] not in dic:
                
                dic[s[right]] = 0
                
            dic[s[right]] += 1
            
            if len(dic) > k:
                
                dic[s[left]] -= 1
                
                if dic[s[left]] == 0:
                    
                    del dic[s[left]]
                    
                left += 1
                
            if len(dic) == k:
                max_length = max(max_length, right - left + 1)
            
            right += 1
            
        
        return max_length
            
            
        