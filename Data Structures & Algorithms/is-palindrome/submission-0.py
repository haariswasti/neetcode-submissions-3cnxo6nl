class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use 2 pointer 
        #read front and back
        c = "".join(ch.lower() for ch in s if ch.isalnum())
        l = 0
        r = len(c) - 1
        while l < r:
            if c[l] != c[r]:
                return False
            l += 1
            r -= 1
        return True