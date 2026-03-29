class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {

        //     //BRUTE FORCE
        //     for (let i = 0; i < nums.length; i++) {
        //         for (let j = 0; j < nums.length; j++) {

        //             if ((i != j) && nums[i] === nums[j]) {
        //                 return true;
        //             }


        //         }
        //     }
        //         return false;


        let newSet = new Set();

        nums.forEach(a => {
            newSet.add(a);
        })


        if(newSet.size !== nums.length)
        {
            return true;
        }
        return false;





    }




}
