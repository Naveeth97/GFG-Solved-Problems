//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while (t-- > 0) {
            String S = in.readLine();

            Solution ob = new Solution();
            System.out.println(ob.maxLength(S));

            System.out.println("~");
        }
    }
}
// } Driver Code Ends



class Solution {
    static int maxLength(String s) {
        // code here
        
        Stack<Integer> stack = new Stack<>();

        // Push -1 as the initial index to
          // handle the edge case
        stack.push(-1);
        int maxLen = 0;

        // Traverse the string
        for (int i = 0; i < s.length(); i++) {

            // If we encounter an opening parenthesis, 
              // push its index
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {

                // If we encounter a closing parenthesis, 
                  // pop the stack
                stack.pop();

                // If stack is empty, push the current index 
                // as a base for the next valid substring
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {

                    // Update maxLength with the current length 
                    // of the valid parentheses substring
                    maxLen = Math.max(maxLen, i - stack.peek());
                }
            }
        }

        return maxLen;
    }
}