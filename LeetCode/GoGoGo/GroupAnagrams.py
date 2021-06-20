class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = dict()
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in dct:
                dct[sortedS] = []
            dct[sortedS].append(s)
        result = []
        for k in dct:
            result.append(dct[k])
        return result
