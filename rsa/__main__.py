import argparse

from .rsa import RSA


def isprime(num: str) -> int:
    """
    Validates if provided number is prime
    """
    try:
        number = int(num)
    except TypeError:
        raise argparse.ArgumentTypeError("Input should be prime number!")
    if number == 1 or number == 2 or number == 3:
        return number
    if number == 4:
       raise argparse.ArgumentTypeError("Input should be prime number!")

    index = 3
    while number > index:
        if number % index == 0:
            raise argparse.ArgumentTypeError("Input should be prime number!")
        else:
            index += 1

    if(index == number):
        return number
    raise argparse.ArgumentTypeError("Input should be prime number!")


def custom_usage() -> str:
    """
    Custom usage message for argparse
    """
    return 'rsa [-h] (-e | -d) [-p] [-q] [-i]'


def parse_args() -> dict:
    """
    Parses arguments from CLI
    """
    parser = argparse.ArgumentParser(description=argparse.SUPPRESS, usage = custom_usage())

    parser.add_argument('-p', type=isprime, metavar="", default=31, help='Prime number used to generate key')
    parser.add_argument('-q', type=isprime, metavar="", default=19, help='Prime number used to generate key')
    parser.add_argument('-i', '--input', type=str, metavar="", help='Input text to encrypt or decrypt.')

    args = vars(parser.parse_args())

    return args


def main() -> None:
    """
    Main function
    """
    args = parse_args()

    # start prompt if input wasn't provided via CLI
    if args['input'] is None:
        args['input'] = input('Input text: ').strip()

    # change input to lower case
    args['input'] = args['input'].lower()

    # create instance of RSA class
    rsa = RSA(args['p'], args['q'])

    # list info about generated values
    rsa.info()
    
    # encrypt and decrypt
    rsa.work(args['input'])


if __name__ == '__main__':
    main()
