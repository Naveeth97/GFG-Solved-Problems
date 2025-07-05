class Solution {
    public int maxSum(int arr[]) {
        
        int maxi = 0;
        
        int len = arr.length;
        
        for(int i = 0; i < len-1; i++)
        {
            int a = arr[i];
            int b = arr[i+1];
            
            maxi = Math.max(maxi, a+b);
        }
        
        return maxi;
    }
}