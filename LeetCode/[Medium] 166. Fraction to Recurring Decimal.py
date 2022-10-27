class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        sign = '' if numerator * denominator > 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)

        res = str(numerator // denominator) + '.'

        numerator %= denominator

        part = ''
        i = 0
        rem_map = {numerator: i}

        while numerator:
            i += 1
            numerator *= 10
            rem = numerator % denominator
            part += str(numerator // denominator)
            if rem in rem_map:
                part = part[:rem_map[rem]] + '(' + part[rem_map[rem]:] + ')'
                break
            rem_map[rem] = i
            numerator = rem
        return sign + res + part
