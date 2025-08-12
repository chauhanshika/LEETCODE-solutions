class Solution:
    def maximumPopulation(self, logs):
        arr = [0] * 101  # years 1950–2050

        for birth, death in logs:
            arr[birth - 1950] += 1
            arr[death - 1950] -= 1

        currpop = 0
        maxpop = 0
        maxYear = 1950

        for i in range(101):
            currpop += arr[i]
            if currpop > maxpop:
                maxpop = currpop
                maxYear = 1950 + i

        return maxYear
