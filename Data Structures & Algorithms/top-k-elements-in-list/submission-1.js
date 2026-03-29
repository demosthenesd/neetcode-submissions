class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        let count = {};


        for (let i = 0; i < nums.length; i++) {

            if (!count[nums[i]]) {
                count[nums[i]] = 1;
            }
            else {

                count[nums[i]]++;
            }

        }
        let sortedEntries = Object.entries(count).sort((a, b) => b[1] - a[1]);


        //console.log(sortedEntries.slice(0, k).map(num => num[1]))
        return (sortedEntries.slice(0, k).map(num => num[0]))





    }
}
