class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = [""]

        for digit in digits:
            new_comb = []

            for combo in combinations:
                for letter in d[digit]:
                    new_comb.append(combo+letter)
            combinations = new_comb
        return combinations




        

        