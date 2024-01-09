//{ Driver Code Starts
//Initial Template for Java





import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            int n = Integer.parseInt(br.readLine().trim());
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            int ans = new Solution().findSum(arr, n);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


//User function Template for Java


class Solution {
    int findSum(int arr[], int n) {
        // code here
        Arrays.sort(arr);
        int arrIndex = 0,sum = arr[0],previousElement = arr[0];
        
        for(int i =1;i<n;i++){
            if((arr[i] != arr[arrIndex]) && (previousElement != arr[i])){
                sum += arr[i];
                previousElement = arr[i];
                arrIndex++;
            }
        }
        return sum;
    }
}