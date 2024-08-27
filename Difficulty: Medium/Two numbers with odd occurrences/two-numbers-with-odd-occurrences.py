#User function Template for python3
class Solution:
    def twoOddNum(self, arr, N):
        # code here
        
        xor = 0
        
        for i in arr:
            
            xor ^= i
            
        bucket_0 = []
        bucket_1 = []
        
        first_bit_num = (xor & xor - 1) ^ xor
        
        for i in range(len(arr)):
            
            if (first_bit_num & arr[i] == 0):
                bucket_0.append(arr[i])
            else:
                bucket_1.append(arr[i])
                
        distinct1 = 0
        distinct2 = 0
        
        for i in bucket_0:
            
            distinct1 ^= i
            
        for i in bucket_1:
            
            distinct2 ^= i
            
        if distinct1 > distinct2:
            
            return [distinct1, distinct2]
            
        return [distinct2, distinct1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends