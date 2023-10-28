#include <vector>
#include <unordered_map>

using namespace std;

/**
 * @brief A solution to find the top k frequent elements in an array.
 * 
 * This class provides a method to find the k most frequent elements
 * in a given array. The method uses a hash map to count the occurrences
 * of each element, and then buckets sort to group elements by their frequency.
 * 
 */
class Solution {
public:
    /**
     * @brief Finds the k most frequent elements in an array.
     * 
     * This method first iterates through the input array, counting the
     * occurrences of each element using a hash map. It then creates a
     * frequency array where each index represents a frequency, and each value
     * is a vector of elements that have that frequency. It finally iterates
     * through the frequency array from highest to lowest frequency, collecting
     * elements until it has found k elements.
     * 
     * @param nums The input array.
     * @param k The number of top frequent elements to find.
     * @return A vector of the k most frequent elements.
     */
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;  // Hash map to count element occurrences.
        vector<vector<int>> freq(nums.size() + 1);  // Frequency array.

        // Count the occurrences of each element.
        for (int n : nums) {
            count[n]++;
        }

        // Bucket sort: place elements into the frequency array based on their count.
        for (auto& [n, c] : count) {
            freq[c].push_back(n);
        }

        vector<int> res;  // Result vector.

        // Collect the k most frequent elements.
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;  // Return early if k elements have been collected.
                }
            }
        }

        return res;  // Return the result vector.
    }
};
