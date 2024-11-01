#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        
        maximum_sum = 0
        
        arr.sort()
        lis = [0] * len(arr)
        # [1, 2, 4, 8]
        i, j = 0, len(arr) - 1
        k = 0
        
        while i <= j:
            
            if k % 2 == 0:
                lis[k] = arr[i]
                i += 1
            else:
                lis[k] = arr[j]
                j -= 1
            k += 1
        
        maximum_sum += abs(lis[0] - lis[len(arr) - 1])
        
        # print(lis)
        k = 1
        while k < len(arr):
            
            maximum_sum += abs(lis[k - 1] - lis[k])
            k += 1
        return maximum_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends