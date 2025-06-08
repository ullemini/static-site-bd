from enum import Enum

class TextType(Enum):
    NORMAL = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = "link"
    IMG = 6



class TextNode():

    def __init__(self,text,text_type,url=None):
        super().__init__()
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, value):
        if self.text != value.text:
            return False
        elif self.text_type != value.text_type:
            return False
        elif self.url != value.url:
            return False
        else: 
            return True


    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"