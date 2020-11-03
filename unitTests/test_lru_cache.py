import unittest

from lru_cache.auxiliary_structures import Node
from lru_cache.cache import LRUCache


class LRUTest(unittest.TestCase):

    def test_lru(self):
        '''
        Test LRU Cache
        '''
        lru = LRUCache(capacity=3)

        # insert all nodes
        lru.put('1', 1)
        lru.put('2', 2)
        lru.put('3', 3)
        lru.put('4', 4)
        lru.put('5', 5)

        # assert that nodes 1, and 2 should be evicted
        self.assertFalse(lru.get('1'))
        self.assertFalse(lru.get('2'))

        # assert the the top priority node is 5
        self.assertEqual(lru.dll.values[0], 5)

        # delete a node
        lru.delete('5')
        self.assertEqual(lru.dll.values[0], 4)


    def test_lru_reset(self):
        '''
        Test LRU reset method
        '''
        lru = LRUCache(capacity=3)

        lru.put('1', 1)
        lru.put('2', 2)

        lru.reset_cache()

        self.assertEqual(lru.dll.values, [])





if __name__ == '__main__':
    unittest.main()
