# https://www.interviewbit.com/problems/letter-phone/

dct = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

def generateAll(inp, result):
    if inp == "":
        return
    if len(inp) == 1:
        result.extend(dct[inp[0]])
        return
    withoutFirst = []
    generateAll(inp[1:], withoutFirst)
    for d in dct[inp[0]]:
        for elem in withoutFirst:
            result.append(d + elem)

class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        result = []
        generateAll(A, result)
        return result
