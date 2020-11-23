class Solution():
    def romanToInt(self,s):
        data = {'I' : 1, 'V':5, 'X':10,'L':50,'C': 100, 'D':500, 'M':1000}
        number = 0
        pos = 0
        for i in range(len(s)-1):
            digit = s[i]
            nextDigit = s[i+1]
            if data[digit] >= data[nextDigit]:
                number += data[digit]
            else:
                number -= data[digit]
        number += data[s[i]]
        return number

a = Solution()
print(a.romanToInt('LVIII'))