import argparse

import playfair as pl

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def len_lt_26(key: str) -> str:
    if len(key) < 26:
        return key.lower()
    raise argparse.ArgumentTypeError("Key must be shorter than 26!")


def parse_args() -> dict:
    parser = argparse.ArgumentParser(description=argparse.SUPPRESS)
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--encrypt', '-e', action='store_true', help='Encrypt text from input.')
    group.add_argument('--decrypt', '-d', action='store_true', help='Decrypt text from input.')
    parser.add_argument('--key', '-k', type=len_lt_26, metavar = "", default='siema', help='Matrix key used for encryption and decryption of the message. [defaults to: siema]')
    parser.add_argument('--text', '-t', type=str, metavar = "", help='Input text to cipher or decipher.')

    args = vars(parser.parse_args())

    return args


def main():
    args = parse_args()

    if args['text'] is None:
        args['text'] = input("Input: ").strip()

    args['text'] = args['text'].lower()
    
    if args['encrypt']:
        pl.Playfair(args['text']).cipher()
    else:
        pl.Playfair(args['text']).decipher()


if __name__ == '__main__':
    main()
