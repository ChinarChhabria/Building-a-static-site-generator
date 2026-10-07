
class HTMLNode():
    def __init__(self,tag:str|None=None,value:str|None=None,children:list|None=None,props:dict[str,str]|None=None)->None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        f_str ="" 
        for i in self.props:
            f_str +=  f" {i.strip('"')}=\"{self.props[i]}\""
        return f_str
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"


class LeafNode(HTMLNode):
    def __init__(self,tag:str,value:str,props:dict=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        elif not self.tag:
            return self.value
        else:
            if self.props:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self,tag:str,children,props:dict=None):
        super().__init__(tag,None,children,props)
    def to_html(self):
        if not self.tag:
            raise ValueError("Doensn't have a tag!!!!")
        elif not self.children:
            raise ValueError("Children don't exist")
        content = ""

        for i in self.children:
            content += i.to_html()
        if self.props:
            return f"<{self.tag}{self.props_to_html}>{content}</{self.tag}>"
        return f"<{self.tag}>{content}</{self.tag}>"
        






    
