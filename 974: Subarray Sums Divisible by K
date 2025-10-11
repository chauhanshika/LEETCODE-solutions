#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> modCount;
        modCount[0] = 1; 

        int prefixSum = 0;
        int result = 0;

        for (int num : nums) {
            prefixSum += num;
            int remainder = prefixSum % k;

           
            if (remainder < 0) remainder += k;

           
            if (modCount.find(remainder) != modCount.end()) {
                result += modCount[remainder];
            }

           
            modCount[remainder]++;
        }

        return result;
    }
};
