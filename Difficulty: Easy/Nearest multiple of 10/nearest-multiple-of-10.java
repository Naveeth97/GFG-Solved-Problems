//{ Driver Code Starts
// Initial Template for Java

// Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;


// } Driver Code Ends
// User function Template for Java
class Solution {

    String roundToNearest(String str) {
        int n = str.length();
        StringBuilder sb = new StringBuilder(str);
        
        int last = sb.charAt(n - 1) - '0';
        sb.setCharAt(n - 1, '0'); // last digit is zero for all the cases
        
        if (last > 5) {
            int idx;
            
            for (idx = n - 2; idx >= 0; idx--) {
                int num = sb.charAt(idx) - '0';
                
                // If the digit is 9, search for the other digits which is not 9 and set it to 0
                if (sb.charAt(idx) == '9') {
                    sb.setCharAt(idx, '0');
                }
                // If the digit is not 9, then set the incremented digit at the index
                else {
                    sb.setCharAt(idx, (char) (num + 1 + '0'));
                    break;
                }
            }
            
            // If all the digits are 9, then set all to zero and insert 1 at beginning
            if (idx == -1) {
                sb.insert(0, '1');
            }
        }
        
        return sb.toString();
    }
}


//{ Driver Code Starts.

// Driver class
class Array {

    // Driver code
    public static void main(String[] args) throws IOException {
        // Taking input using buffered reader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testcases = Integer.parseInt(br.readLine());

        // looping through all testcases
        while (testcases-- > 0) {

            String str = br.readLine().trim();

            Solution obj = new Solution();

            String res = obj.roundToNearest(str);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends