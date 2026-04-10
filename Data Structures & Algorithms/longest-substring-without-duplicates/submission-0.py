class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        l = 0
        long = 0
        for ran in range(len(s)):
            while s[ran] in ans:
                ans.remove(s[l])
                l += 1
            
            ans.add(s[ran])
            long = max(long, ran - l + 1)

        return long