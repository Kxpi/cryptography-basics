import argparse

from .playfair import Playfair


def key_type(key: str) -> str:
    """
    Validates if provided key is shorter than 26 chars and if it consists of unique letters (only letters)
    """
    if len(key) < 26 \
    and sorted(list(set(key))) == sorted(list(key)) \
    and key.isalpha():
        return key.lower().replace(' ', '')
    raise argparse.ArgumentTypeError("Key must be shorter than 26 characters and consist only of unique letters!")


def custom_usage() -> str:
    """
    Custom usage message for argparse
    """
    return 'playfair [-h] (-e | -d) [-k] [-i]'


def parse_args() -> dict:
    """
    Parses arguments from CLI
    """
    parser = argparse.ArgumentParser(description=argparse.SUPPRESS, usage = custom_usage())

    # encryption ad decryption are mutually exclusive - only one canm be performed at the time
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-e', '--encrypt', action='store_true', help='Encrypt text from input.')
    group.add_argument('-d', '--decrypt', action='store_true', help='Decrypt text from input.')
    parser.add_argument('-k', '--key', type=key_type, metavar="", default='siema', help='Key word used for encryption and decryption of the message. [defaults to: siema]')
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

    print(f'\nInput: {args["input"]} \nKey: {args["key"]}\n')

    if args['encrypt']:
        Playfair(args['input'], args['key'], DEBUG = True).encrypt()
    else:
        Playfair(args['input'], args['key'], DEBUG = True).decrypt()


if __name__ == '__main__':
    main()
