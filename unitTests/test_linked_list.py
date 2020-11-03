import unittest

from lru_cache.auxiliary_structures import Node, DoubleLinkedList


class DoubleLinkedListTest(unittest.TestCase):

    def test_dll_insertions(self):
        '''
        Test insertions
        '''
        dll = DoubleLinkedList()
        dll.insert_node(Node('a', 1))
        dll.insert_node(Node('b', 2))
        true_values = [2, 1]
        expected_values = dll.values
        self.assertEqual(true_values, expected_values)


    def test_dll_deletions(self):
        '''
        Test deletions
        '''
        dll = DoubleLinkedList()


        a , b = Node('a', 1), Node('b', 2)
        dll.insert_node(a)
        dll.insert_node(b)

        # delete once
        dll.delete_node(a)

        # delete again
        self.assertFalse(dll.delete_node(a))

        true_values = [2]
        expected_values = dll.values
        self.assertEqual(true_values, expected_values)


if __name__ == '__main__':
    unittest.main()
