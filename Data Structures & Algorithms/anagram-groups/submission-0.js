class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

        let storage = {};

        for (var i = 0; i < strs.length; i++) {

            let sorted = strs[i].split("").sort().join("");

            if (!storage[sorted]) {
                storage[sorted] = [];
            }

            storage[sorted].push(strs[i]);



        }

        return (Object.values(storage));


    }
}
