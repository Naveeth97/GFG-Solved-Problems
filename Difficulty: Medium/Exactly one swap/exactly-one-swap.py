class Solution:
    def countStrings(self, s): 
        #code here
        
        mpp = [0] * 26
        
        ans = 0
        
        for i in range(len(s)):
            
            ans += (i - mpp[ord(s[i]) - ord('a')])
            mpp[ord(s[i]) - ord('a')] += 1
            
        for i in mpp:
            
            if i > 1:
                return ans + 1
                
        return ans