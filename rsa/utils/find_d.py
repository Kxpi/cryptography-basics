from random import randint
from .isPrime import isPrime
from .coprime import coprime


def find_d(e, phi):
    d = 1
    while not ((e * d - 1) % phi == 0):
        d = randint(1, phi)
    return d