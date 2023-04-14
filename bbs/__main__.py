import argparse

from .bbs import BBS
from .tests import Tests


def custom_usage() -> str:
    """
    Custom usage message for argparse
    """
    return 'bbs [-h] [-l] [-t]'


def parse_args() -> dict:
    """
    Parses arguments from CLI
    """
    parser = argparse.ArgumentParser(description=argparse.SUPPRESS, usage = custom_usage())

    parser.add_argument('-l', '--length', type=int, default=20000, help='Number of bits.')
    parser.add_argument('-t', '--test', action='store_true', help='Perform tests.')

    args = vars(parser.parse_args())

    return args


def main() -> None:
    """
    Main function
    """
    args = parse_args()

    bits = BBS(33359,67967)
    bits = bits.generateBits(args['length'])

    if args['test']:
        Tests().single_bit(bits)
        Tests().series(bits)
        Tests().longest_series(bits)
        Tests().poker(bits)



if __name__ == '__main__':
    main()
