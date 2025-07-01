class Solution:
    def substrCount(self, s, k):
        # code here
        
        alpha = [0] * 26
        
        left = 0
        right = 0
        
        n = len(s)
        res = 0
        
        cnt = 0
        
        while right < n:
            
            if alpha[ord(s[right]) - 97] == 0:
        
                cnt += 1
            
            alpha[ord(s[right]) - 97] += 1
                
            while right - left + 1 > k  or cnt > k - 1:
                
                alpha[ord(s[left]) - 97] -= 1
                
                if alpha[ord(s[left]) - 97] == 0:
                    
                    cnt -= 1
                    
                left += 1
                
            if right - left + 1 == k and cnt == k - 1:
                
                res += 1
                
            right += 1
                
        return res
                
                
                
        