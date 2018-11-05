"""
TRIE data structure.

"""

import os, sys

class Node():
    def __init__(self):
        self.data = {}
        self.flag = None


def insert(root, word):
    node = root
    index_last_char = None
    for i, ch in enumerate(word):
        if ch in node.data:
            node = node.data[ch]
        else:
            index_last_char = i
            break
    # append new nodes for the remaining cahr, if any
    if index_last_char != None:
        for ch in word[index_last_char: ]:
            node.data[ch] = Node()
            node = node.data[ch]
    node.flag = True

def find(node, strs):
    for ch in strs:
        if ch in node.data:
            node = node.data[ch]
        else:
            return None
    return node.flag


root = Node()
insert(root, 'sunny')
insert(root, 'sun')
#insert(root, 'sunyy')
print("inserted all words")
#print(root.data)
print("finding word:")
print(find(root, 'sun'))


"""

#-------- Trie implementation ----------

"""
class TrieNode():
    def __init__(self):
        self.value = None
        self.children = dict()

class Trie:

    def __init__(self):
        self.root  = TrieNode()

    def insert(self, word):
        insert(self.root, word)

    def search(self, word):
        return bool(find(self.root, word))

    def startsWith(self, prefix):
        return bool(starts_with(self.root, word))

def starts_with(node, key):
    node = find(node, key)
    return bool(node)

def find(node, prefix):
    for ix, c in enumerate(prefix):
        if c in node.children:
            node =  node.children[c]
        else:
            return None
    return node

def insert(node, key):
    last_index_character = None
    for idx, c in enumerate(key):
        if c in node.children:
            node = node.children[c]
        else:
            last_index_character = idx
            break

    if last_index_character is not None:
        for c in key[last_index_character:]:
            node.children[c] = TrieNode()
            node = node.children[c]
    node.value = key


def lexicographic_order(node):
    if node.value:
        print(node.value)

    for k, v in sorted(node.children.items(), key=lambda x: x[0]):
        lexicographic_order(v)


def delete(node, key, original_key=None):
    original_key = original_key or key
    if not key:
        return

    c = key[0]
    if node.children:
        delete(node.children[c], key[1:], original_key)

    if (node.children.get(c, None) and not node.children[c].children):
        if original_key == node.children[c].value or not node.children[c].value:
            del node.children[c]


def build_trie(words):
    root = TrieNode()
    for w in words:
        insert(root, w)
    return root

