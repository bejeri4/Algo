# https://www.interviewbit.com/problems/word-ladder-i/

import queue
from string import ascii_lowercase

def getNeigs(word, allWords):
    result = []
    for i in range(len(word)):
        for ch in ascii_lowercase:
            if ch == word[i]:
                continue
            neig = word[:i] + ch + word[i + 1:]
            if neig in allWords:
                result.append(neig)
    return result

def bfs(start, end, words):
    if start == end:
        return 0
    words.add(end)
    visited = set()
    q = queue.Queue()
    visited.add(start)
    q.put((start, 1))
    while not q.empty():
        curWord, curD = q.get()
        if curWord == end:
            return curD
        for neig in getNeigs(curWord, words):
            if neig not in visited:
                visited.add(neig)
                q.put((neig, curD + 1))
    return 0


class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        return bfs(A, B, set(C))
