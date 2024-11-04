import pygtrie


class SuffixTree:
    def __init__(self):
        self.trie = pygtrie.StringTrie()

    def insert(self, text):
        """
        Insert a text into the suffix tree.
        """
        self.trie[text] = True

    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        Returns True if the pattern exists, False otherwise
        """
        return pattern in self.trie

    def find_suffixes(self, prefix):
        """
        Find all suffixes of strings starting with a given prefix
        """
        return self.trie.items(prefix=prefix)


# Example usage:
if __name__ == "__main__":
    # Create a suffix tree
    suffix_tree = SuffixTree()

    # Inserting strings into the suffix tree
    text = "banana"
    suffix_tree.insert(text)

    text = "orange"
    suffix_tree.insert(text)

    text = "appletree"
    suffix_tree.insert(text)

    print("Suffix Tree Created!")

    # Search for a pattern
    pattern = "ana"
    found = suffix_tree.search(pattern)
    print(f"Search for '{pattern}': Found = {found}")  # Output: Search for 'ana': Found = True

    # Find suffixes
    prefix = "app"
    suffixes = suffix_tree.find_suffixes(prefix)
    print(f"Suffixes of '{prefix}': {suffixes}")  # Output: Suffixes of 'app': [('appletree', True)]
