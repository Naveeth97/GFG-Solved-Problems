//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        while (t-- > 0) {
            String[] arr1Str = sc.nextLine().split(" ");
            int[] arr = Arrays.stream(arr1Str).mapToInt(Integer::parseInt).toArray();
            int target = Integer.parseInt(sc.nextLine());

            Solution ob = new Solution();
            int ans = ob.countTriplets(arr, target);
            System.out.println(ans);
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {
    public int countTriplets(int[] arr, int target) {
        // Code Here
        int count = 0;
        
        for (int i = 0; i < arr.length; i++) {
            
            int left = i + 1;
            int right = arr.length - 1;
            
            while (left < right) {
                
                if ((arr[i] + arr[left] + arr[right]) == target) {
                    count += 1;
                    
                    int dup_left = left + 1;
                    int dup_right = right;
                    
                    while (dup_left < dup_right && ((arr[i] + arr[dup_left] + arr[dup_right]) == target)) {
                        count++;
                        dup_left++;
                    }
                    
                    dup_left = left;
                    dup_right = right - 1;
                    
                    while (dup_left < dup_right && ((arr[i] + arr[dup_left] + arr[dup_right]) == target)) {
                        count++;
                        dup_right--;
                    }
                    
                    left++;
                    right--;
                } else if ((arr[i] + arr[left] + arr[right]) < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return count;
    }
}