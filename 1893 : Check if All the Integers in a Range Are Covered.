class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        box = [0] * 52
        for l,r in ranges:
            box[l] +=1
            box[r+1] -= 1
        coverage = 0
        for i in range(1,52):
            coverage += box[i]
            if left <= i <= right and coverage<=0:
                return False
        return True
