class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # speed = distance / time
        # time = distance / speed
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        fleet = currMax = currTime = 0
        for p,s in pair:
            currTime = (target - p) / s
            if currTime > currMax:
                currMax = currTime
                fleet += 1


        return fleet