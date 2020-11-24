import math

def decimalToBinary(decimal):
    if decimal == 0:
        return "0"
    result = ""
    d = abs(decimal)
    while d != 0:
        b = d % 2
        result += str(b)
        d //= 2
    if decimal < 0:
        result += "-"
    return result[::-1]
    
    
def binaryToDecimal(binary):
    if not binary:
        return None
    b = binary
    if binary[0] == "-":
        if len(binary) == 1:
            return None
        b = b[1:]
    result = 0
    b = b[::-1]
    for i in range(len(b)):
        if b[i] == "1":
            result += int(math.pow(2, i))
    if binary[0] == "-":
        result = -result
    return result
