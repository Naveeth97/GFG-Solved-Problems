//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;

class DriverClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int[][] arr = new int[n][n];

            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) arr[i][j] = sc.nextInt();

            GFG g = new GFG();
            g.rotate(arr);
            printMatrix(arr);

            System.out.println("~");
        }
    }

    static void printMatrix(int arr[][]) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) System.out.print(arr[i][j] + " ");
            System.out.println("");
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class GFG {
    static void rotate(int mat[][]) {
        // Code Here
        
        int rows = mat.length;
        int columns = mat[0].length;
        
        for (int i = 0; i < rows; i++) {
            for (int j = i + 1; j < columns; j++) {
                swap(i, j, mat);
            }
        }
        
        for (int i = 0; i < rows; i++) {
            reverse(i, columns, mat);
        }
    }
    
    private static void swap(int fir, int lst, int[][] matrix) {
        
        int temp = matrix[fir][lst];
        matrix[fir][lst] = matrix[lst][fir];
        matrix[lst][fir] = temp;
    }
    
    private static void reverse(int row, int col, int[][] matrix) {
        
        int temp;
        
        int trav = 0;
        int revTrav = col - 1;
        
        while (trav < revTrav) {
            
            temp = matrix[row][trav];
            matrix[row][trav] = matrix[row][revTrav];
            matrix[row][revTrav] = temp;
            trav++;
            revTrav--;
        }
    }
}