class Playfair:
    def __init__(self, input_text: str) -> None:
        self.text = input_text


    def cipher(self) -> None:
        non_spaced = Playfair.remove_spaces(self.text)
        fixed_text = Playfair.fix_text(non_spaced)
        print(fixed_text)


    def decipher(self) -> None:
        print(self.text[::-1])


    @staticmethod
    def remove_spaces(text: str) -> str:
        words = text.split()
        non_spaced_text = ''.join(words)
        return non_spaced_text


    @staticmethod
    def fix_text(text: str) -> str:
        index = 0
        while (index<len(text)):
            letter1 = text[index]
            if index == len(text)-1:
                text = text + 'x'
                index += 2
                continue
            letter2 = text[index+1]
            if letter1==letter2:
                text = text[:index+1] + "x" + text[index+1:]
            index +=2   
        return text