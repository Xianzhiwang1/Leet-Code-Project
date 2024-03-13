class Colors{
    public void sortColors(int[] nums) {
        if (nums.length == 0 || nums.length == 1) return;
        int start = 0;
        int end = nums.length - 1;
        int index = 0;

        while (index <= end && start < end) {
            if ( nums[index] == 0) {
                nums[index] = nums[start];
                nums[start] = 0;
                start++;
                index++;
            } else if (nums[index] == 2)  {
                nums[index] = nums[end];
                nums[end] = 2;
                end--;
            } else {
                index++;
            }
        }
            


    }
    public static void main(String[] args) {
        int[] nums = new int[]{2,0,2,1,1,0};
        Colors mysoln  = new Colors();
        mysoln.sortColors(nums);
        System.out.println("Hello World!");
        System.out.println(nums.toString());
}

}
