#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> modIndex;
        modIndex[0] = -1; // remainder 0 seen before starting index (for subarray from 0)

        long long prefixSum = 0;

        for (int i = 0; i < nums.size(); i++) {
            prefixSum += nums[i];

            int remainder;
            if (k != 0)
                remainder = prefixSum % k;
            else
                remainder = prefixSum; // when k == 0, just keep prefix sum

            if (remainder < 0) remainder += k; // handle negative values

            // If same remainder was seen before, check distance
            if (modIndex.find(remainder) != modIndex.end()) {
                if (i - modIndex[remainder] > 1)
                    return true; // subarray length ≥ 2
            } else {
                // store first occurrence of this remainder
                modIndex[remainder] = i;
            }
        }

        return false;
    }
};
