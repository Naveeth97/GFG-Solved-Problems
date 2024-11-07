#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        
        total_sum = 0
        
        for i in range(len(arr)):
            
            total_sum += arr[i]
            
        if total_sum % 3 != 0:
            
            return [-1, -1]
            
        current_sum = 0
        
        target = total_sum // 3
        
        ans = []
        
        for i in range(len(arr)):
            
            if len(ans) == 2:
                return ans
            
            current_sum += arr[i]
            
            if current_sum == target:
                ans.append(i)
                
                current_sum = 0
                
        if len(ans) == 2:
            return ans
            
        return [-1, -1]
                
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends