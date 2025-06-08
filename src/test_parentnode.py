import unittest
from htmlnode import ParentNode,LeafNode

class TestParentNode(unittest.TestCase):    
    
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
    def test_multichild_Parent_node(self):
        child_node_1 = LeafNode("b", "Bold text")
        child_node_2 = LeafNode(None, "Normal text")
        child_node_3 = LeafNode("i", "italic text")
        child_node_4 = LeafNode(None, "Normal text")
        node = ParentNode(
            "p",
            [
                child_node_1,
                child_node_2,
                child_node_3,
                child_node_4
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
            )

    def test_to_html_with_multiple_grandchildren(self):

        grandchild_node_b = LeafNode("b", "grandchild_b")
        grandchild_node_n = LeafNode(None, "grandchild_n")
        child_node_span = ParentNode("span", [grandchild_node_b,grandchild_node_n])
    
        grandchild_node_i = LeafNode("i", "grandchild_i")
        child_node_p = ParentNode("p",[grandchild_node_i])

        parent_node = ParentNode("div", [child_node_span,child_node_p])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild_b</b>grandchild_n</span><p><i>grandchild_i</i></p></div>"
            )

    def test_parent_whith_parent_prop(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span></div>"
        )