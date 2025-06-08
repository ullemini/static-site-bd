import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        #bold test
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        #ITALIC test
        ITALIC_node = TextNode("This is a text node", TextType.ITALIC)
        ITALIC_node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(ITALIC_node,ITALIC_node2)
        #Code test
        code_node = TextNode("This is a text node", TextType.CODE)
        code_node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(code_node,code_node2)

        # other tests
        self.assertNotEqual(node,ITALIC_node)
        self.assertNotEqual(node,code_node)
        self.assertNotEqual(code_node,ITALIC_node)

        url_node = TextNode("This is a text node", TextType.CODE,"www.url.se")
        self.assertNotEqual(url_node,node)


        


if __name__ == "__main__":
    unittest.main()