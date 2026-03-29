class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {


        // check if the have the same length 
        if (s.length !== t.length) {
            return false;
        }


        let hash_s = {};
        let hash_t = {};

        for (let i = 0; i < s.length; i++) {

            hash_s[s[i]] = 1 + (hash_s[s[i]] || 0);
            hash_t[t[i]] = 1 + (hash_t[t[i]] || 0);

        }

        for (const key in hash_s) {
            if (hash_s[key] !== hash_t[key]) { return false; }
        }
        return true;

        // console.log("s: ", hash_s);
        // console.log("t: ", hash_t);



    }
}
