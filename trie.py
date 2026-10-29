# insert(self, key: str, obj: Any) -> None: associates obj with key and indexes
# each word of the key in the trie. Add appropriate validation for key, including malformed
# or empty keys.
import re
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.all_objects = []
    

    def insert(self, key, obj):
        current = self.root
        words = key.split()

        for word in words:
            current = self.root
            for i, char in enumerate(word):
                if char not in current.children:
                    prefix = word[0: i + 1]
                    current.children[char] = TrieNode(prefix)
                current = current.children[char]
            
            current.object.append(obj)
            self.all_objects.append(obj)


    def search_by_prefix(self, prefix):
        if prefix == "":
            return self.all_objects

        result = []
        seen = set()
        current = self.root

        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        def dfs(node):
            for obj in node.object:
                if id(obj) not in seen:
                    result.append(obj)
                    seen.add(id(obj))

            for child in node.children.values():
                dfs(child)

        dfs(current)
        return result



class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        self.object = []