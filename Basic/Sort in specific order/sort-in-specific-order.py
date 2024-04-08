#User function Template for python3

class Solution:
    def sortIt(self, arr, n):
        #code here.
        even = []
        odd = []
        
        for i in range(n):
            
            if(arr[i] % 2 == 1):
                
                odd.append(arr[i])
            else:
                even.append(arr[i])
                
        odd.sort(reverse=True)
        even.sort()
        
        i = 0
        # j = n - 1
        
        for j in range(len(odd)):
            
            arr[i] = odd[j]
            i+=1
            
        for j in range(len(even)):
            
            arr[i] = even[j]
            i+=1
            
        return arr
        
            
            
                
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends