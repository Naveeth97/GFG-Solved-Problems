//{ Driver Code Starts
// Initial Template for Java.
import java.io.*;
import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Reading number of test cases (t)
        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {

            String arr[] = br.readLine().split(" ");
            int prices[] = new int[arr.length];

            for (int i = 0; i < arr.length; i++) {
                prices[i] = Integer.parseInt(arr[i]);
            }

            // Create an instance of the Solution class
            Solution ob = new Solution();

            // Call the stockBuyAndSell method
            int res = ob.maximumProfit(prices);

            // Print the result
            System.out.println(res);

            // Print the "~" symbol to match the original output
            // System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java
class Solution {
    public int maximumProfit(int prices[]) {
        // code here
        
        int maxProfit = 0;
        
        int currStock = prices[0];
        int getStock = prices[0];
        
        for (int i = 1; i < prices.length; i++) {
            
            if (prices[i] <= currStock) {
                maxProfit += (currStock - getStock);
                getStock = prices[i];
                currStock = prices[i];
            } else {
                currStock = prices[i];
            } 
            
        }
        
        if (currStock - getStock > 0) {
            maxProfit += currStock - getStock;
        }
        
        return maxProfit;
    }
}