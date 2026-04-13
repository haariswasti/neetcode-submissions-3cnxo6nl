class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use 2 pointer 
        #read front and back
        a = "".join(char for char in s if char.isalnum())
        l = 0
        r = len(a) -1
        while l < r:
            if a[r].lower() != a[l].lower():
                return False
            l += 1
            r -= 1
        return True