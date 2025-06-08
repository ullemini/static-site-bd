from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = "link"
    IMAGE = 6



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
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT :
                return LeafNode(None,text_node.text)
            case TextType.BOLD:
                return LeafNode("b",text_node.text)
            case TextType.ITALIC:
                return LeafNode("i",text_node.text)
            case TextType.CODE:
                return LeafNode("code",text_node.text)
            case TextType.LINK:
                return LeafNode("i",text_node.text,{"herf":text_node.url})
            case TextType.LINK:
                return LeafNode("i","",{"src":text_node.url,"alt":text_node.text})
            case _:
                raise ValueError(f"invalid text type: {text_node.text_type}")