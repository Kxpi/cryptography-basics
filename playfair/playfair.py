from pprint import pprint

class Playfair:

    def __init__(self, input_text: str, input_key: str, DEBUG: bool = False) -> None:
        self.DEBUG = DEBUG
        self.text = input_text
        self.ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.key = self.__create_key_matrix(input_key)


    def encrypt(self) -> str:
        """
        Function encypts provided input accordingly to specified key
        """
        # normalize text
        non_spaced = self.__remove_spaces()
        fixed_text = self.__fix_text(non_spaced)

        encrypted = ''
        # iterate using pairs of letters
        for (letter1, letter2) in zip(fixed_text[0::2], fixed_text[1::2]):
            # find indexes of rows and columns for both letters
            r1, c1 = self.__get_index(letter1)
            r2, c2 = self.__get_index(letter2)

            if c1 == c2: # letters are in the same column
                encrypted += self.key[(r1+1)%5][c1] + self.key[(r2+1)%5][c2]
            elif r1 == r2: # letters are in the same row
                encrypted += self.key[r1][(c1+1)%5] + self.key[r2][(c2+1)%5]
            else: # letters are in diffetent rows and columns
                encrypted += self.key[r1][c2] + self.key[r2][c1]

        if self.DEBUG:
            print(f'\nEncrypted text: {encrypted}\n')

        return encrypted


    def decrypt(self) -> str:
        """
        Function decrypts provided input accordingly to specified key
        """
        # normalize text
        non_spaced = self.__remove_spaces()
        fixed_text = self.__fix_text(non_spaced)

        decrypted = ''
        # iterate using pairs of letters
        for (letter1, letter2) in zip(fixed_text[0::2], fixed_text[1::2]):
            # find indexes of rows and columns for both letters
            r1, c1 = self.__get_index(letter1)
            r2, c2 = self.__get_index(letter2)

            if c1 == c2: # letters are in the same column
                decrypted += self.key[(r1-1)%5][c1] + self.key[(r2-1)%5][c2]
            elif r1 == r2: # letters are in the same row
                decrypted += self.key[r1][(c1-1)%5] + self.key[r2][(c2-1)%5]
            else: # letters are in diffetent rows and columns
                decrypted += self.key[r1][c2] + self.key[r2][c1]

        if self.DEBUG:
            print(f'\nDecrypted text: {decrypted}\n')

        return decrypted


    def __create_key_matrix(self, input_key: str) -> list:
        """
        Creates key matrix using word provided by user in input
        """
        # initial list to keep track of already present letters
        letters = []
        # empty matrix 5x5
        key_matrix = [[0 for _ in range(5)] for _ in range(5)]
        # replace j with i
        input_key = input_key.replace('j', 'i')

        row, col = 0, 0
        # add letters from input to initial list
        for letter in input_key:
            if letter not in letters:
                key_matrix[row][col] = letter
                letters.append(letter)
            else:
                continue
            if (col == 4):
                col = 0
                row += 1
            else:
                col += 1

        # add rest of alphabet to initial list
        for letter in self.ALPHABET:
            if letter not in letters:
                letters.append(letter)

        letter_idx = 0

        # fill matrix with letters from initial list
        for r in range(5):
            for c in range(5):
                key_matrix[r][c] = letters[letter_idx]
                letter_idx += 1

        if self.DEBUG:
            print('Key matrix:')
            pprint(key_matrix)

        return key_matrix


    def __remove_spaces(self) -> str:
        """
        Removes spaces from text
        """
        non_spaced_text = self.text.replace(' ', '')
        return non_spaced_text


    def __fix_text(self, text: str) -> str:
        """
        Fixes same letters next ot each others, adds x if lentgh of string is odd
        """
        idx = 0
        while (idx<len(text)):
            letter1 = text[idx]
            if idx == len(text) - 1:
                text = text + 'x'
                idx += 2
                continue
            letter2 = text[idx + 1]
            if letter1 == letter2:
                text = text[:idx + 1] + "x" + text[idx + 1:]
            idx += 2   
        return text


    def __get_index(self, letter: str) -> tuple:
        """
        Finds index of row and column of given letter in key matrix
        """
        for i in range (5):
            try:
                idx = self.key[i].index(letter)
                return (i, idx)
            except:
                continue
