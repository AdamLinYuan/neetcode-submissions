#Use a carry?
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        carry = 1
        i = len(digits) - 1

        while carry == 1:

            if digits[i] == 9:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0,1)
                    return digits
                else:
                    digits[i] = 0
                    i -= 1
            else:
                digits[i] += 1
                carry = 0
                return digits


        