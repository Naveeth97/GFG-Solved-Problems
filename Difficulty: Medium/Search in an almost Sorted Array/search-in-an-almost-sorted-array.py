#{ 
 # Driver Code Starts

# } Driver Code Ends

#User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

        # Check mid
            if arr[mid] == target:
                return mid

        # Check mid - 1 (with bounds check)
            if mid > start and arr[mid - 1] == target:
                return mid - 1

        # Check mid + 1 (with bounds check)
            if mid < end and arr[mid + 1] == target:
                return mid + 1

        # Adjust search range
            if target < arr[mid]:
                end = mid - 2
            else:
                start = mid + 2

        return -1

                    
                    
                    


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())  # Number of test cases

    for _ in range(t):
        arr = list(map(int, input().strip().split()))  # Read the array
        target = int(input().strip())  # Read the target

        sln = Solution()
        ans = sln.findTarget(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends