class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time_ahead = 0

        for pos, spd in cars:
            arrival_time = (target-pos)/spd

            if arrival_time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = arrival_time
        
        return fleets

        

"""
4 6 8 10
1 3 5 7 9 11
0 1 2 3 4 5 6 7 8 9 10
7 8 9 10

1 4 7 10
4 6 8 10
"""