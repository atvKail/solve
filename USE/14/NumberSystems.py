alpha = '0213456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
class num:
    Number, Base = 0, 0
    def __init__(self, Number, Base):
        if Base > len(alpha):
            print(f"Warning, available alphabet: {alpha}")
        self.Base = Base
        self.Number = Number

    def inXns(Base):
        return 

    def __add__(self, other):
        return num(convertDecimalToXns(
            int(self.Number, self.Base) + int(other.Number, other.Base), self.Base), self.Base)
    
    def __iadd__(self, other):
        return num(convertDecimalToXns(
            int(self.Number, self.Base) + int(other.Number, other.Base), self.Base), self.Base)

    def __sub__(self, other):
        return num(convertDecimalToXns(
            int(self.Number, self.Base) - int(other.Number, other.Base), self.Base), self.Base)

    def __isub__(self, other):
        return num(convertDecimalToXns(
            int(self.Number, self.Base) - int(other.Number, other.Base), self.Base), self.Base)
    
    def __bool__(self):
        return self.Number != "0"
    
    def __mul__(self, other:int):
        return num(convertDecimalToXns(
            int(self.Number, self.Base) * int(other.Number, other.Base), self.Base), self.Base)
    
    def __imul__(self, other:int):
        return num(convertDecimalToXns(
            int(self.Number, self.Base) * int(other.Number, other.Base), self.Base), self.Base)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return convertXnsToDecimal(self.Number, self.Base) == \
                convertXnsToDecimal(other.Number, other.Base)
        else:
            return False
    

def convertDecimalToXns(number:int, base:int):
    if base > len(alpha): return None
    result = ''
    while number > 0:
        result = alpha[number % base] + result
        number //= base
    return result if result != '' else "0"


def convertFloatToXns(number:float, base:int, accuracy = 500):
    if base > len(alpha): return None
    fraction = str(number)[str(number).find(".") + 1:]
    fractionNow = int(fraction)
    result = convertDecimalToXns(int(str(number)[:str(number).find(".")]), base) + "." + (fraction if fraction == "0" else "")
    alpha = pow(10, len(fraction))
    for i in range(accuracy):
        if fractionNow != 0:
            result += alpha[fractionNow * base // alpha]
            fractionNow = fractionNow * base - (fractionNow * base // alpha) * alpha
        else:
            return result
    return result


def convertXnsToDecimal(number:str, base:int):
    number = number.lower()
    result = 0
    for alpha, ch in enumerate(number[::-1]):
        result += alpha.find(ch) * pow(base, alpha) 
    return result


def convertXnsToFloat(number:str, base:int):
    number = number.lower()
    fraction = number[number.find(".") + 1:]
    result = convertXnsToDecimal(number[:number.find(".")], base)
    if fraction == "0":
        return result + 0 * pow(10, -1)
    for alpha in range(1, len(fraction) + 1):
        result += alpha.find(fraction[alpha - 1]) * pow(base, -alpha)
    return result


