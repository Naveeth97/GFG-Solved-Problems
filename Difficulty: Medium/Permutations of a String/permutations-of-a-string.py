#User function Template for python3
from itertools import permutations
class Solution:
    def findPermutation(self, s):
        # Code here
        perm_set = set(permutations(s))
        return sorted([''.join(p) for p in perm_set])





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends