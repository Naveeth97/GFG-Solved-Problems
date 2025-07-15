class Solution {
    public boolean divby13(String s) {
        int n = s.length();
        
        if (n < 10) return Integer.parseInt(s) % 13 == 0;
        
        char arr[] = s.toCharArray();
        while (n >= 10) {
            int toAdd = (arr[n - 1] - '0') * 4;
            int i = n - 2;
            int carry = 0;
            while (carry > 0 || toAdd > 0) {
                int sum = arr[i] - '0' + toAdd % 10 + carry;
                arr[i--] = (char)('0' + (sum % 10));
                carry = sum / 10;
                toAdd /= 10;
            }
            n--;
        }
        
        return Integer.parseInt(new String(arr, 0, n)) % 13 == 0;
    }
}