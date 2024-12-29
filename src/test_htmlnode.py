import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode1 = HTMLNode(tag="Huh?", value="huhhhh?", props={"href": "https://www.google.com", "target": "_blank",})
        htmlnode2 = HTMLNode(tag="Huh?", value="huhhhh?", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(htmlnode1, htmlnode2)

    def test_typing(self):
        htmlnode1 = HTMLNode(tag="Huh?", value="huhhhh?", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertIsInstance(htmlnode1, HTMLNode)

    def test_repr(self):
        htmlnode1 = HTMLNode(tag="Huh?", value="huhhhh?", props={"href": "https://www.google.com", "target": "_blank",})
        test = repr(htmlnode1)
        self.assertEqual(test, "HTMLNode(tag=Huh?, value=huhhhh?, children=None, props=dict_values(['https://www.google.com', '_blank']))")

    def test_empty(self):
        htmlnode1 = HTMLNode()
        htmlnode2 = HTMLNode()
        self.assertEqual(htmlnode1, htmlnode2)

    def test_props_to_html(self):
        htmlnode1 = HTMLNode(tag="Huh?", value="huhhhh?", props={"href": "https://www.google.com", "target": "_blank",})
        test = htmlnode1.props_to_html()
        self.assertEqual(test, " href=https://www.google.com target=_blank")