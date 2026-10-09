from textnode import TextNode,TextType
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for i in old_nodes:
        if not isinstance(text_type,TextType):
            new_nodes.append(i)
        else:
            match delimiter:
                case "**":
                    delim_type = TextType.BOLD_TEXT
                case "`":
                    delim_type = TextType.CODE_TEXT
                case "_":
                    delim_type = TextType.ITALIC_TEXT
                case _:
                    return "invalid type of delimiter"

            if i.text_type==TextType.TEXT:
                string1 = i.text
                if string1.count(delimiter)%2!=0:
                    raise Exception("The following Node isn't valid because it doesn't close a delimiter")
                else:
                    texts = i.text.split(delimiter)
                    i = 0 
                    while i < len(texts):
                        if texts[i]=="":
                            pass
                        elif i%2==0:
                            new_nodes.append(TextNode(texts[i],TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(texts[i],delim_type))
                        i+=1
            else:
                new_nodes.append(i)
    return new_nodes


