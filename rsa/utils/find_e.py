from random import randint
from .isPrime import isPrime
from .coprime import coprime


def find_e(phi):
    e=2
    while not (isPrime(e) and coprime(e, phi)):
        e = randint(1, phi)
    return e