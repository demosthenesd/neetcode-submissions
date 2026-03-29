class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {

        let left = 0, right = numbers.length - 1;

        let sum = 0;


        while (left < right) {
            sum = numbers[left] + numbers[right]

            if (sum > target) right -= 1
            else if (sum < target) left += 1

            else return [left + 1, right + 1]

        }
        return []



    }
}
