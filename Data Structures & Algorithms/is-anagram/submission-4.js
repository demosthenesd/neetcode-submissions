class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        // // BRUTE FORCE
        // let sortedT = t.split("").sort().join("");
        // let sortedS = s.split("").sort().join("");

        // if (sortedT === sortedS) return true;

        // return false;

        const t_count = {};
        const s_count = {};

        for (let i = 0; i < s.length; i++) {
            s_count[s[i]] = (s_count[s[i]] || 0) + (1);
            t_count[t[i]] = (t_count[t[i]] || 0) + 1;
        }


        for (const charCount in s_count) {
            if (s_count[charCount] !== t_count[charCount]) {
                return false;
            }
        }

        return true;

        //console.log("S: ", s_count);




    }
}
