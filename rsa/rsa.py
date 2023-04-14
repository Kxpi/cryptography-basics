from .utils import find_d, find_e

class RSA:

    def __init__(self, p: int, q: int, DEBUG: bool = True) -> None:
        self.DEBUG = DEBUG
        self.n = p * q
        self.phi = (p-1)*(q-1)
        self.e = find_e.find_e(self.phi)
        self.d = find_d.find_d(self.e, self.phi)
        

    def info(self):
        """
        Lists values (phi, n, e, d) generated during initialization
        """
        print(f'''
        Phi: {self.phi}

        Public key:
        e = {self.e}    
        n = {self.n}

        Private key:
        d = {self.d}     
        n = {self.n}''')


    def work(self, message: str, return_encrypted: bool = True) -> str:
        """
        Encrypts and decrypts provided message
        
        return_encrypted when set to True, returns result of encryption
        """
        encrypted_nums = self.__encoder(message)
        encrypted = ''.join(str(p) for p in encrypted_nums)
        decrypted = ''.join(self.__decoder(encrypted_nums))

        if self.DEBUG:
            print(f'''
        Original message:
        {message}

        Encrypted:
        {encrypted}

        Decrypted:
        {decrypted}''')
        
        if return_encrypted:
            return encrypted
        

    def __single_encrypt(self, letter: int) -> int:
        """
        Function encrypts signle letters
        """
        c = (letter ** self.e) % self.n

        return c


    def __single_decrypt(self, letter: int) -> int:
        """
        Function decrypts single letters
        """
        m = (letter ** self.d) % self.n

        return m


    def __encoder(self, message: str) -> list:
        """
        Converts message to list with ascii codes and encrypts them
        Returns list of encoded values
        """
        encoded = []
        for letter in message:
            encoded.append(self.__single_encrypt(ord(letter)))
        return encoded
    
    
    def __decoder(self, encoded: str) -> list:
        """
        Converts message to list with ascii codes and decrypts them
        Returns list of decoded values
        """
        decoded = []
        for num in encoded:
            decoded.append(chr(self.__single_decrypt(num)))
        return decoded