import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf1 = LeafNode(tag="a", value="link", props={"href": "https://www.google.com", "target": "_blank",})
        leaf2 = LeafNode(tag="a", value="link", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(leaf1, leaf2)
