class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the order
        #check 

        store = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in store:
                store[key].append(s)

            else:
                store[key] = [s]
                
        return list(store.values())


  