from googletrans import Translator

# This class translates all conversations to Lithuanian language
class LT_translate:
    def __init__(self, input_get: str):

        self.translator = Translator()
        self.input_get = input_get
    
    def translate_input_lt(self) -> str:
        result = self.translator.translate(self.input_get, dest='lt')
        print(result.text)
        return result.text