import unittest
from textnode import TextNode,TextType
from markdown_to_textnode import split_nodes_delimiter



class TESTTYPE(unittest.TestCase):

    def test_bold(self):
        test1 = [TextNode("**whatever** is this", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            [
                TextNode("whatever", TextType.BOLD_TEXT),
                TextNode(" is this", TextType.TEXT)
            ]
        )

    def test_bold_at_start(self):
        test1 = [TextNode("**bold** text", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            [
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_bold_at_end(self):
        test1 = [TextNode("text **bold**", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            [
                TextNode("text ", TextType.TEXT),
                TextNode("bold", TextType.BOLD_TEXT)
            ]
        )

    def test_bold_only(self):
        test1 = [TextNode("**bold**", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            [TextNode("bold", TextType.BOLD_TEXT)]
        )

    def test_multiple_bold_sections(self):
        test1 = [TextNode("**one** and **two**", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            [
                TextNode("one", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.BOLD_TEXT)
            ]
        )

    def test_italic(self):
        test1 = [TextNode("_italic_ text", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "_", TextType.ITALIC_TEXT),
            [
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_italic_only(self):
        test1 = [TextNode("_italic_", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "_", TextType.ITALIC_TEXT),
            [TextNode("italic", TextType.ITALIC_TEXT)]
        )

    def test_multiple_italic_sections(self):
        test1 = [TextNode("_one_ and _two_", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "_", TextType.ITALIC_TEXT),
            [
                TextNode("one", TextType.ITALIC_TEXT),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.ITALIC_TEXT)
            ]
        )

    def test_italic_at_start(self):
        test1 = [TextNode("_italic_ text", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "_", TextType.ITALIC_TEXT),
            [
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_italic_at_end(self):
        test1 = [TextNode("text _italic_", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "_", TextType.ITALIC_TEXT),
            [
                TextNode("text ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC_TEXT)
            ]
        )

    def test_code(self):
        test1 = [TextNode("Use `print()` here", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "`", TextType.CODE_TEXT),
            [
                TextNode("Use ", TextType.TEXT),
                TextNode("print()", TextType.CODE_TEXT),
                TextNode(" here", TextType.TEXT)
            ]
        )

    def test_code_only(self):
        test1 = [TextNode("`print()`", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "`", TextType.CODE_TEXT),
            [TextNode("print()", TextType.CODE_TEXT)]
        )

    def test_code_at_start(self):
        test1 = [TextNode("`x = 5` is code", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "`", TextType.CODE_TEXT),
            [
                TextNode("x = 5", TextType.CODE_TEXT),
                TextNode(" is code", TextType.TEXT)
            ]
        )

    def test_code_at_end(self):
        test1 = [TextNode("This is `code`", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "`", TextType.CODE_TEXT),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE_TEXT)
            ]
        )

    def test_empty_list(self):
        test1 = []
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            []
        )

    def test_empty_text(self):
        test1 = [TextNode("", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            []
        )

    def test_no_delimiter(self):
        test1 = [TextNode("plain text", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            [TextNode("plain text", TextType.TEXT)]
        )

    def test_unmatched_delimiter(self):
        test1 = [TextNode("**bold text", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT)

    def test_empty_delimited_text(self):
        test1 = [TextNode("****", TextType.TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            []
        )

    def test_non_text_node(self):
        test1 = [TextNode("already bold", TextType.BOLD_TEXT)]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            [TextNode("already bold", TextType.BOLD_TEXT)]
        )

    def test_multiple_nodes(self):
        test1 = [
            TextNode("**bold**", TextType.TEXT),
            TextNode("plain text", TextType.TEXT),
            TextNode("*italic*", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter(test1, "**", TextType.BOLD_TEXT),
            [
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode("plain text", TextType.TEXT),
                TextNode("*italic*", TextType.TEXT)
            ]
        )

new = TESTTYPE()
new.test_empty_delimited_text()