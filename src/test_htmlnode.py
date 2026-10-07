import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test1 = HTMLNode(None,None,None,{
        "href": "https://www.google.com",
        "target": "_blank",
        })
        text = test1.props_to_html()
        self.assertEqual(text," href=\"https://www.google.com\" target=\"_blank\"")
        test2 = HTMLNode(None,None,None,{
            "href": "https://www.github.com",
            "target": "_blank",
        })
        text = test2.props_to_html()
        self.assertNotEqual(text," href=\"https://www.google.com\" target=\"_blank\"")
        test3 = HTMLNode(None,None,None,{
                    "href": "https://www.google.com",
                })
        self.assertEqual(test3.props_to_html()," href=\"https://www.google.com\"")

    def test_Leaf_to_html_p(self):
            node = LeafNode("p", "Hello, world!")
            self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
            node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            self.assertEqual(node2.to_html(),'<a href="https://www.google.com">Click me!</a>')
            node3 = LeafNode("h","Whats up gang")
            self.assertEqual(node3.to_html(),'<h>Whats up gang</h>')
            
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        





            
            
            