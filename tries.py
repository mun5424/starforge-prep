"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

The Trie gets asked pretty often in an interview as it is extremely efficient when it comes to searching an index or a word.
Tries are generally 
insert - O(k)
delete - O(k)
Search - O(k) where k is length of the string queried 

"""
class TrieNode:
    def __init__(self): 
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word: 
            if w not in curr.children: 
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isWord = True
            
        
    def search(self, word: str) -> bool:
        curr = self.root
        for w in word: 
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix: 
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True


trie = Trie() 

trie.insert("jujutsu")
trie.insert("kaizen")
print(trie.search("kaizen")) # true
print(trie.search("onepiece")) # false
print(trie.startsWith("juju")) # true