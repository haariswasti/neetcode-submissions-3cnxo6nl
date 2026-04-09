class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the order
        #check 
        ans = {}


        for s in strs:
            key = "".join(sorted(s))

            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]

            
            

        return list(ans.values())

  