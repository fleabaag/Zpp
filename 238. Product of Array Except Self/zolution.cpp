#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> leftProduct(n, 1);  // Producto acumulado desde la izquierda
        vector<int> rightProduct(n, 1);  // Producto acumulado desde la derecha
        vector<int> result(n);  // Vector resultado

        // Calcular el producto acumulado desde la izquierda
        for (int i = 1; i < n; ++i) {
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
        }

        // Calcular el producto acumulado desde la derecha
        for (int i = n - 2; i >= 0; --i) {
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
        }

        // Combinar los productos acumulativos para obtener el resultado final
        for (int i = 0; i < n; ++i) {
            result[i] = leftProduct[i] * rightProduct[i];
        }

        return result;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    vector<int> result = sol.productExceptSelf(nums);
    for (int i : result) {
        cout << i << " ";
    }
    return 0;
}
