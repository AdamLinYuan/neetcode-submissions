class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []

        for p,s in pair:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
            #If the current car takes less time to arrive than the previous car then we remove the current car as we want to keep the slowest cars ahead as thats what forms a fleet
                stack.pop()

        return len(stack)