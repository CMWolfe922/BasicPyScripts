import asyncio
import os, sys

"""
The Node class will contain data. It will hold data that will then be 
passed to the stack class. The Stack class will then store the data
until it is needed. When the data is needed, it will pop the data 
from the stack and then the data can be used however it is needed. 

One example will be making each company symbol a Node object and then 
passing each Node to the stack. Once there, I can pop one Node at a 
time and execute multiple data collection functions on each Node. I can 
repeat this process until there are no more Nodes in the Stack. 
"""

class Node:

    def __init__(self, data = None):
        # a Node in a linked list holds data and a real reference to
        # the next item in the linked list. 
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        # Create a new node
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                # check if there is more than one node.
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            print("Stack is empty")

    def peek(self):
        """
        :use: Works like a pop operation except the peek operation
        just returns the top element but does not delete it from 
        the stack. The peek method allows you to view the top.
        """
        if self.top:
            return self.top.data
        else:
            print("Stack is empty")