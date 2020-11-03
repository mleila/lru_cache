# -*- coding: utf-8 -*-
'''This module hosts implementations of caches.'''

from .auxiliary_structures import Node, DoubleLinkedList


class LRUCache:


    # private methods
    def _prioritize(self, node):
        '''
        Move node to priority position
        '''
        self.dll.delete_node(node)
        self.dll.insert_node(node)


    def _pop(self):
        '''
        Pop the last node in the dll
        '''
        last_node = self.dll.tail.prev
        self.dll.delete_node(last_node)
        return last_node


    # initialization
    def __init__(self, capacity:int):
        '''
        '''
        self.size = 0
        self.dict = {}
        self.capacity = capacity
        self.dll = DoubleLinkedList()


    # public methods
    def get(self, key):
        '''
        '''
        node = self.dict.get(key, None)
        if node is None:
            return

        # move the accessed node to the head;
        self._prioritize(node)

        return node.value


    def put(self, key, value):
        '''
        '''
        node = self.dict.get(key)

        if node is None:
            # create new node
            node = Node(key, value)
            # add to dict
            self.dict[key] = node
            # insert into dll
            self.dll.insert_node(node)
            # increment the size
            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                last_node = self._pop()
                del self.dict[last_node.key]
                self.size -= 1
            return

        # override node value
        node.value = value

        # inset into dll
        self.dll.insert_node(node, head=True)


    def delete(self, key):

        # assert key is in dict
        assert key in self.dict, f'{key} not in cache'

        node = self.dict[key]
        self.dll.delete_node(node)
        del self.dict[key]
        self.size -= 1


    def reset_cache(self):
        '''
        Remove all items from cache
        '''
        self.__init__()
