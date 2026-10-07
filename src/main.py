from textnode import TextNode,TextType


def main():
    obj = TextType.LINKS
    print(TextNode("this is some text",obj,"https://www.boot.dev"))

if __name__ == "__main__":
    main()
