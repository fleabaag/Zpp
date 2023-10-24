#include <unordered_map>
#include <vector>
using namespace std;

/**
 * @class Solution
 * @brief A class to solve the Two Sum problem.
 */
class Solution {
public:

    /**
     * @brief Finds two indices i and j in a vector such that nums[i] + nums[j] equals the target value.
     * @param nums A reference to the vector of integers.
     * @param target The target sum we're looking to achieve.
     * @return A vector containing the two indices that sum to the target value, or an empty vector if no such indices exist.
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        // Iterate through the vector with a nested loop to check all pairs of indices.
        for (size_t i = 0; i < nums.size(); i++) {
            for (size_t j = i + 1; j < nums.size(); j++) {
                // If the sum of the elements at indices i and j equals the target value, return these indices.
                if (nums[i] + nums[j] == target) {
                    return {static_cast<int>(i), static_cast<int>(j)};
                }
            }
        }
        // Return an empty vector if no such indices are found.
        return {};
    }
};
