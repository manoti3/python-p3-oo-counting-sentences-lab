#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    def get_value(self):
        return self._value
    def set_value(self, string):
        if type(string) is str:
        # if isinstance(string, str):
            self._value = string
        else:
            print('The value must be a string.')
    value = property(get_value, set_value)

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False
        
    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False
        
    def count_sentences(self):
        for punc in ['!', '?']:
            self.value = self.value.replace(punc, '.')
        result_list = self.value.split('.')
        # print(result_list)
        # for sentence in result_list:
        #     if sentence == "":
        #         # print(sentence)
        #         result_list.remove(sentence)
        # print(result_list)
        # return len(result_list)
        result_list = [s for s in result_list if s != '']
        print(len(result_list))
        return len(result_list)
    
# complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
# complex_string.count_sentences()