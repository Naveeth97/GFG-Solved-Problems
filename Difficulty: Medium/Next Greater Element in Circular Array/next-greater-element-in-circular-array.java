class Solution {
    public ArrayList<Integer> nextLargerElement(int[] nums) {
        // code here
        
        Stack<Integer> stack = new Stack<>();

        int n = nums.length;

        for (int i = n - 2; i >= 0; i--) {

            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }

            stack.push(i);
        }

        int[] res = new int[n];

        for (int i = n - 1; i >= 0; i--) {

            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }

            res[i] = stack.isEmpty() ? -1 : nums[stack.peek()];
            stack.push(i);
        }
        
        ArrayList<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < res.length; i++) {
            
            ans.add(res[i]);
        }
        
        return ans;
    }
}