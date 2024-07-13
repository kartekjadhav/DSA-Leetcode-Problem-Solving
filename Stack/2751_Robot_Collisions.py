#TC - O(NLOGN), SC - O(N)
from typing import List
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robot_map = {pos:robot for robot,pos in enumerate(positions)}
        positions.sort()
        stack = []
        for position in positions:
            robot = robot_map[position]
            if directions[robot]=='R':
                stack.append(robot)
            else:
                while stack and healths[robot]!=-1:
                    last_robot = stack.pop()
                    if healths[last_robot]>healths[robot]:
                        healths[last_robot] -=1
                        healths[robot] = -1
                        stack.append(last_robot)
                    elif healths[last_robot]<healths[robot]:
                        healths[last_robot] = -1
                        healths[robot] -=1
                    else:
                        healths[last_robot] = healths[robot] = -1
        
        return [health for health in healths if health!=-1]