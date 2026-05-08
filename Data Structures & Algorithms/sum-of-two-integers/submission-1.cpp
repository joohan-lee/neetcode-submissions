class Solution {
public:
    int getSum(int a, int b) {
        int sum_without_carry;
        int carry;
        while (b != 0){
            sum_without_carry = a ^ b;
            carry = (a & b) << 1;
            a = sum_without_carry;
            b = carry;
        }
        return a;
        
    }
};
