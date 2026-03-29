class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let numSet = new Set(nums);
        let longest = 0;

        for (let num of numSet) {
            // Check if it's the start of a sequence
            if (!numSet.has(num - 1)) {
                let length = 1;
                let currentNum = num;

                while (numSet.has(currentNum + 1)) {
                    currentNum++;
                    length++;
                }

                longest = Math.max(longest, length);
            }
        }

        return longest;
    }
}
