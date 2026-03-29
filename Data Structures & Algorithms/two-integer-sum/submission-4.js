class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        let set_nums = new Map();


        for (let i = 0; i < nums.length; i++) {

            let diff = target - nums[i];

            if (set_nums.has(diff)) {
                return [set_nums.get(diff), i]
            }

            set_nums.set(nums[i], i);


        }






        //BRUTE FORCE - SOLVED MYSELF WEEE

        // for (let i = 0; i < nums.length; i++) {
        //     for (let j = 0; j < nums.length; j++) {

        //         if ((i != j) && (nums[i] + nums[j]) === target) {

        //             return ([i, j])

        //         }




        //     }

        // }



    }
}
