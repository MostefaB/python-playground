# 853. Car Fleet
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        # Pair car position with speeds
        cars = [[pos,speed] for pos, speed in zip(position,speed)]
        print(f" --- Cars(position, speed): {cars}")
        # Sort using position
        cars.sort()
        print(f" --- Sorted Cars(position, speed): {cars}")
        stack = list()

        for i in range(n - 1, -1, -1):
            car = cars[i]
            nb_hours_to_target = (target - car[0]) / car[1]
            stack.append(nb_hours_to_target)
            # Check stack and pop if there is a collision between the second to last and the last car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(Solution().carFleet(target, position, speed))
