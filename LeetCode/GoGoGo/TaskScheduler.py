class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1
        freq.sort()
        top = freq.pop()
        same = 0
        while freq:
            curTop = freq.pop()
            if top == curTop:
                same += 1
            else:
                break
        titalTime = top + (top - 1) * n + same
        return max(titalTime, len(tasks))
