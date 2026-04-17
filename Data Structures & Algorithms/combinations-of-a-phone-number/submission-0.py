class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        sub = []
        ans = []
        phone = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno",
        "7": "pqrs","8": "tuv","9": "wxyz" }

        def backtrack(i):
            if i == len(digits):
                ans.append("".join(sub))
                return
            for c in phone[digits[i]]:
                sub.append(c)
                backtrack(i + 1)
                sub.pop()
        backtrack(0)
        return ans
            

        