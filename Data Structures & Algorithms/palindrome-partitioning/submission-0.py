class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def isPal(sub):
            return sub == sub[::-1]

        def backtrack(start):
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start, len(s)):
                sub = s[start:end + 1]

                if isPal(sub):
                    path.append(sub)
                    backtrack(end + 1)
                    path.pop()
        backtrack(0)
        return ans
