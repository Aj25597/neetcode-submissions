class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 0
        for i in range(len(digits)-1,-1,-1):
            digit = digits[i]
            digit = digit + 1
            if digit > 9:
                digits[i] = 0
            else:
                digits[i] = digit
                break
        if digit > 9:
            digits.insert(0,1)
        return digits


        