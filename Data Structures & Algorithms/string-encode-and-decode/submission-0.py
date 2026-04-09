class Solution:

    def encode(self, strs: List[str]) -> str:
        dec = ""
        for s in strs:
            dec += str(len(s)) + "#" + s 
        return dec
        

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1

            word = s[i: i+length]
            ans.append(word)

            i = i + length
        return ans


        

