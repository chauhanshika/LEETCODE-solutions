class Solution:
    def numPairsDivisibleBy60(self, time):
        rem_count = [0] * 60
        ans = 0
        for t in time:
            r = t % 60
            comp = (60 - r) % 60
            ans += rem_count[comp]
            rem_count[r] += 1
        return ans
