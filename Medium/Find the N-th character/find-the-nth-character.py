#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        
        res = ''
        
        for i in range(r):
            
            for j in s:
                if(j == '1'):
                    res += '10'
                else:
                    res += '01'
                    
                if(len(res) > n):
                    break
                
            s = res
            res = ''
        return s[n]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends