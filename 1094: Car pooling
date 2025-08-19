class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1001

        for passengers, start, end in trips:
            timeline[start] += passengers
            timeline[end] -= passengers

        current = 0
        for change in timeline:
            current += change
            if current > capacity:
                return False

        return True
