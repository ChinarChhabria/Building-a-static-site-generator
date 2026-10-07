from enum import Enum
import typing
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINKS = 'links'
    IMAGES = "images"

class TextNode():
    def __init__(self,text:str,text_type:TextType,URL:str=None)->None:
        self.text = text
        self.text_type=text_type
        self.url = URL
    def __eq__(self,other)->bool:
        if self.text ==other.text and self.text_type==other.text_type and self.url == other.url:
            return True
        else:
            return False
    def __repr__(self)->str:
        return f"TextNode({self.text},{self.text_type},{self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i",text_node)
        case TextType.CODE_TEXT:
            return LeafNode("code",text_node)
        case TextType.LINKS:
            return LeafNode("a",text_node,{"href":text_node.url})
        case TextType.IMAGES:
            return LeafNode("img","",{"src":text_node.url,"alt":"IDC"})
        case _:
            raise Exception("Invalid Input")
        
