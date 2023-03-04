# cryptography-basics
Algorithms implementation from "Cryptography basics" uni course.

# Requirements
As of this commit, all algorithms are written in vanilla python without any additional dependecies.

# Usage
Algorithms are stored in sub-directories - they were implemented in a way that they are treated as python modules (so remember about **```-m```** flag!). Here is how to run an algorithm from root-level directory of this repo:

```
python3 -m <algorithm name> [flags]
```
For example:
```
python3 -m playfair --encrypt --input 'message' --key 'key'
```

# Algorithms

## Playfair
* Usage:
    ```
    $ python3 -m playfair --help
        usage: playfair [-h] (-e | -d) [-k] [-i]

        optional arguments:
          -h, --help     show this help message and exit
          -e, --encrypt  Encrypt text from input.
          -d, --decrypt  Decrypt text from input.
          -k , --key     Key word used for encryption and decryption of the message. [defaults to: siema]
          -i , --input   Input text to encrypt or decrypt.
    ```
* Encryption:
    ``` 
    $ python3 -m playfair --encrypt -i 'message' -k 'key'
    ```
* Decryption:
    ``` 
    $ python3 -m playfair --decrypt -i 'lyxaxgda' -k 'key'
    ```
* Note: only one operation is allowed at a time - encryption or decryption!
    ```
    python3 -m playfair -d -e
        usage: playfair [-h] (-e | -d) [-k] [-i]
        __main__.py: error: argument -e/--encrypt: not allowed with argument -d/--decrypt
    ```