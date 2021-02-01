# https://www.interviewbit.com/problems/shortest-unique-prefix/

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        
        
def insertWord(head, word):
    if word == "":
        return
    if word[0] not in head.children:
        newNode = Node(word[0])
        head.children[word[0]] = newNode
    child = head.children[word[0]]
    insertWord(child, word[1:])


def findPrefix(head, word, i, lastSplitIndex):
    if i == len(word):
        return word[:lastSplitIndex + 1]
    if len(head.children) > 1:
        lastSplitIndex = i
    return findPrefix(head.children[word[i]], word, i + 1, lastSplitIndex)


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        head = Node("")
        for elem in A:
            insertWord(head, elem)
        result = [""] * len(A)
        for i in range(len(A)):
            result[i] = findPrefix(head, A[i], 0, 0)
        return result
