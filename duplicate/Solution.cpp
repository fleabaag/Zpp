using namespace std;
#include <vector>
#include <algorithm>

class Solution
{
public:
    /**
     * Dice si un arreglo contiene elementos duṕlicados.
     *
     * @param  nums El arreglo a recorrer.
     * @return True si contiene algún elemento duplicado, False en otro caso.
     */
    bool containsDuplicate(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 1; i++)
            if (nums[i] == nums[i + 1])
                return true;

        return false;
    }
};