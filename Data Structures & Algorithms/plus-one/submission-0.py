class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1 , -1):
            new = digits[i] + carry
            carry = 1 if new > 9 else 0
            digits[i] = 0 if carry else new
        
        if carry:
            digits.insert(0, carry)

        return digits