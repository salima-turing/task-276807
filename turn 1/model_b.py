# Importing the suffix tree library
from suffix_trees import STree

# Creating a suffix tree instance
suffix_tree = STree.STree()


### Inserting a Sequence into the Suffix Tree:
def insert_sequence(sequence):
    # The suffix_tree.insert method requires a sequence and an optional identifier (default is None)
    suffix_tree.insert(sequence)


# Example sequence
sequence = "GATATATGCATATACTT"
insert_sequence(sequence)


### Searching for a Subsequence in the Suffix Tree:
def search_sequence(pattern):
    # The suffix_tree.find method returns the list of starting indices of the occurrences of the pattern in the sequence.
    occurrences = suffix_tree.find(pattern)
    return occurrences


# Example pattern to search
pattern = "ATAT"
result = search_sequence(pattern)

if result:
    print(f"Found pattern '{pattern}' at indices: {result}")
else:
    print(f"Pattern '{pattern}' not found in the sequence.")
