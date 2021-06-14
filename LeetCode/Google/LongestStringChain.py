from functools import cmp_to_key

def isChain(a, b):
	if len(b) - 1 != len(a):
		return False
	for i in range(len(b)):
		if a == b[:i] + b[i + 1:]:
			return True
	return False

def tryToMakechain(words, i, j, chainLens):
	if isChain(words[i], words[j]):
		chainLens[j] = max(chainLens[i] + 1, chainLens[j])

def cmp(a, b):
    return len(a) - len(b)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = cmp_to_key(cmp))
        chainLens = [1] * len(words)
        print(words, "a")
        for i in range(len(words)):
            j = i + 1
            while j < len(words):
                if len(words[j]) == len(words[i]):
                    j += 1
                elif len(words[j]) - 1 == len(words[i]):
                    tryToMakechain(words, i, j, chainLens)
                    print(i, j)
                    j += 1
                else:
                    break
        return max(chainLens)
