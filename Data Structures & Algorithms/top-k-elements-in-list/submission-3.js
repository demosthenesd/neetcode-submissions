class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        let countOfNums = {};


        for (let i = 0; i < nums.length; i++) {

            if (!countOfNums[nums[i]]) {
                countOfNums[nums[i]] = 1;

            }
            else {
                countOfNums[nums[i]]++;
            }


        }

        let answer = [];

        let sortedArray = Object.entries(countOfNums).sort(([, a], [, b]) => (a - b)).reverse().slice(0, k);
        // let sortedArray = Object.entries(countOfNums).sort().reverse();

        console.log(sortedArray)

        for (const [key, val] of (sortedArray)) {

            answer.push(key);
        }



        return answer;




    }
}
