from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)
        
        for x in strs:
            word = ''.join(sorted(x))
            mp[word].append(x)
        
        return list(mp.values())