class Solution:
    def romanToInt(self, s):

        tiers = {"I": 0, "V": 1, "X": 2, "L": 3 ,"C": 4, "D": 5, "M": 6}
        vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0

        for i in range(len(s) - 1):
            if tiers[s[i]] < tiers[s[i + 1]]:
                total -= vals[s[i]]

            else:
                total += vals[s[i]]

        total += vals[s[-1]]

        return total