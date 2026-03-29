class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let totalProduct = 1;
        let zeroCount = 0;

        // Compute total product while counting zeroes
        for (let num of nums) {
            if (num !== 0) {
                totalProduct *= num;
            } else {
                zeroCount++;
            }
        }

        return nums.map(num => {
            if (zeroCount > 1) {
                return 0; // More than one zero means all products are zero
            } else if (zeroCount === 1) {
                return num === 0 ? totalProduct : 0; // Only the zero position gets the product
            } else {
                return Math.floor(totalProduct / num); // Integer division
            }
        });
    }
}