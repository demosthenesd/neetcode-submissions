class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {

        //low hanging check
        if (s.length !== t.length) return false;

        let sortedT = t.split("").sort().join("");
        let sortedS = s.split("").sort().join("");



        if (sortedT === sortedS) return true;

        return false;






    }
}
