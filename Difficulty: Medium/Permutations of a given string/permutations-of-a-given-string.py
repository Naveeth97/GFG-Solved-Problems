#User function Template for python3

class Solution:
    def find_permutation(self, s):
        # Code here
        lis = []
        self.helper("", s, lis)
        
        return lis
        
    def helper(self, process, un_process, lis):
        
        if len(un_process) == 0:
            
            if process not in lis:
                lis.append(process)
            return
        
        for i in range(len(process) + 1):
            
            fir = process[0 : i]
            sec = process[i : len(process)]
            
            self.helper(fir + un_process[0] + sec, un_process[1:], lis)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.find_permutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends