class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # speed = distance / time
        # time = distance / speed
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        time = []
        for p,s in pair:
            distance= target - p
            time.append(distance/s)
        fleet = currMax = 0
        for t in time:
            if t > currMax:
                fleet += 1
                currMax = t

        return fleet