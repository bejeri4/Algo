class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        buckets = []
        for _ in range(26):
            buckets.append([])
        for word in words:
            index = ord(word[0]) - ord("a")
            buckets[index].append(word)
        for ch in s:
            index = ord(ch) - ord("a")
            newBucket = []
            for word in buckets[index]:
                if not word[1:]:
                    result += 1
                else:
                    newIndex = ord(word[1]) - ord("a")
                    if index == newIndex:
                        newBucket.append(word[1:])	
                    else:
                        buckets[newIndex].append(word[1:])
            buckets[index] = newBucket
        return result
