class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        dir = 0
        for i in instructions:
            if i == "G":
                if dir == 0:
                    y += 1
                elif dir == 1:
                    x += 1
                elif dir == 2:
                    y -= 1
                else:
                    x -= 1
            elif i == "L":
                dir = (dir - 1) % 4
            else:
                dir = (dir + 1) % 4
        return (x == 0 and y == 0) or dir != 0
