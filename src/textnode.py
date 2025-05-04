from enum import Enum

class TextType(Enum):
    
    def __init__(self,text,text_type,url):
        super().__init__()
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value):
        return super().__eq__(value)
    
    
    def __repr__(self):
        return super().__repr__()

    