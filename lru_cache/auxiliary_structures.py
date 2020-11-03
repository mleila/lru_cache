# -*- coding: utf-8 -*-
'''This module hosts implementations of different auxiliary data structures.'''

from typing import List


class Node:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:

    def __init__(self):
        self.head = Node(key='head', value=None)
        self.tail = Node(key='tail', value=None)

        # connect the head to the tail
        self.head.next = self.tail
        self.tail.prev = self.head


    @property
    def keys(self)->List:
        '''
        Return a list of node keys
        '''
        keys = []
        node = self.head.next
        if node is None:
            return keys

        while node != self.tail:
            curr_key = node.keys
            keys.append(curr_key)
            node = node.next

        return keys


    @property
    def values(self)->List:
        '''
        Return a list of node values
        '''
        values = []
        node = self.head.next
        if node is None:
            return values

        while node != self.tail:
            curr_value = node.value
            values.append(curr_value)
            node = node.next

        return values


    def insert_node(self, node: Node, head: bool=True):
        '''
        insert a new node to the Double Linked List (DLL).

        Args:
        - node: object of class Node
        - head: if true, the DLL inserts the node after the head,
                else the node is inserted before the tail

        Return:
        None
        '''
        target = self.head if head else self.tail
        node.prev = target
        node.next = target.next
        target.next.prev = node
        target.next = node


    def delete_node(self, node):
        '''
        Delete a node from the Double Linked List (DLL).

        Args:
        - node: node to be deleted

        Return:
        - True if the deletion was successful otherwise flase
        '''
        prev = node.prev
        temp = node.next
        prev.next = temp
        temp.prev = prev
