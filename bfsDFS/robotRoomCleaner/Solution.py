
class Solution:
    def cleanRoom(self, robot):
        def dfs(robot,cpos,cdir) :
            visited.add(cpos)
            robot.clean()
            for i in range(4):
                nextDir = (cdir + i) % 4
                npos = (cpos[0] + steps[nextDir][0] , cpos[1] + steps[nextDir][1]) 
                if npos not in visited and robot.move() :
                    dfs(robot,npos,nextDir)
                    # cant move forward in same direction so go back to previous position and direction
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()
        steps = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        dfs(robot,(0,0),0)
   