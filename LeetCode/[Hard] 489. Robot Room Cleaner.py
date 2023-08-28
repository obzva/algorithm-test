# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def turn_back():
            robot.turnRight()
            robot.turnRight()

        def go_backward():
            turn_back()
            robot.move()
            turn_back()

        # direction :
        #   0: up 1: right 2: down 3: left
        def backtrack(cell, direction):
            robot.clean()
            visited.add(cell)
            for i in range(4):
                new_direction = (direction + i) % 4
                new_cell = (
                    cell[0] + deltas[new_direction][0],
                    cell[1] + deltas[new_direction][1],
                )
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_direction)
                    go_backward()
                robot.turnRight()

        backtrack((0, 0), 0)

        # Time complexity
        ## backtrack -> 4 times of iteration for each cell
        ## we visit only non-obstacle cells once
        ### O(N - M) where N is the total number of cells and M is the number of obstacle cells

        # Space complexity
        ## visited -> O(N - M)
        ### O(N - M)
