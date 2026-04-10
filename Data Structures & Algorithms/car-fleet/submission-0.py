class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse = True)

        fleets = 0
        solw = 0

        for pos, sped in cars:
            time = (target -pos)/sped

            if time > solw:
                fleets += 1
                solw = time
        return fleets

        

