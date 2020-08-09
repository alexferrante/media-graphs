import json

import attr
import cattr
import typing
from typing import Type, TypeVar, Generic

@attr.s(auto_attribs=True)
class Node():
    name: str = ""
    children: typing.List[Node] = attr.Factory(list)
    parents: typing.List[Node] = attr.Factory(list)
    info: str = ""
    url: str = ""

    def __init__(self, name, info):
        self.name = name
        self.info = info

    
    def remove_child(self, child_node):
        self.children = [c for c in self.children if c == child_node]
    

    def remove_parent(self, parent_node):
        self.parents = [p for p in self.parents if p == parent_node]

    