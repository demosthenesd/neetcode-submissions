class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {

        const newSet = new Set();


        for (let i = 0; i < nums.length; i++) {

            newSet.add(nums[i]);
        }

        console.log(newSet.length);

        if (newSet.size !== nums.length) return true;

        return false;





        //BRUTE FORCE -- worked my self WEE

        // for (let i = 0; i < nums.length; i++) {
        //     for (let j = 1; j < nums.length; j++) {

        //         if ((i != j) && nums[i] === nums[j]) {
        //             return true;
        //         }


        //     }
        // }
        // return false;


    }
}
