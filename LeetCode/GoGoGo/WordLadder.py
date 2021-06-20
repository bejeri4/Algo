import queue

def getNeigs(word, st):
	result = []
	for i in range(len(word)):
		for j in range(26):
			ch = chr(ord("a") + j)
			newWord = word[:i] + ch + word[i + 1:]
			if newWord in st:
				result.append(newWord)
	return result
		

def bfs(start, end, st):
	visited = set()
	q = queue.Queue()
	visited.add(start)
	q.put((start, 1))
	while not q.empty():
		word, d = q.get()
		if word == end:
			return d
		neigs = getNeigs(word, st)
		for neig in neigs:
			if neig not in visited:
				q.put((neig, d + 1))
				visited.add(neig)
	return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        return bfs(beginWord, endWord, st)
