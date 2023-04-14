from random import randint
from .utils.isPrime import isPrime
from .utils.coprime import coprime


class BBS:
    p = 0
    q = 0
    n = 0
    generatedValues = []

    def __init__(self, p, q):
        self.setP(p)
        self.setQ(q)
        if(self.p > 0 and self.q > 0):
            self.__setN()

    def setP(self, p):
        if(not self.__checkParams(p)):
            self.p = p

    def setQ(self, q):
        if(not self.__checkParams(q)):
            self.q = q

    def __checkParams(self, number):
        isError = False
        if(not isPrime(number)):
            print(number, 'is not prime')
            isError = True

        return isError

    def __setN(self):
        self.n = self.p * self.q

    def __generateValue(self):
        if(self.p > 0 and self.q > 0):
            x = 0
            while (not coprime(self.n, x)):
                x = randint(1, self.n)
            return pow(x, 2) % self.n

    def generateBits(self, amount):
        if(self.p == self.q):
            print('p should be diffrent than q')
            return False

        if (self.n == 0):
            print('N is equal 0')
            return False

        else:
            bitsArray = []

            for _ in range(amount):
                generatedValue = self.__generateValue()
                self.generatedValues.append(generatedValue)

                if(generatedValue % 2 == 0):
                    bitsArray.append(0)
                else:
                    bitsArray.append(1)

            return bitsArray