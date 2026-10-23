"""Build a Huffman tree and print a binary code for each character."""

import heapq
from itertools import count


class Node:
    def __init__(self, character=None, frequency=0, left=None, right=None):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right


number_of_characters = int(input("Enter number of characters: "))
heap = []
unique_id = count()  # Break ties safely when two frequencies are equal.

for _ in range(number_of_characters):
    character = input("Enter character: ")[0]
    frequency = int(input("Enter frequency: "))
    if frequency < 0:
        raise ValueError("Frequency cannot be negative.")

    node = Node(character=character, frequency=frequency)
    heapq.heappush(heap, (frequency, next(unique_id), node))

if not heap:
    print("No characters were provided.")
else:
    # Repeatedly combine the two least-frequent nodes.
    while len(heap) > 1:
        left_frequency, _, left_node = heapq.heappop(heap)
        right_frequency, _, right_node = heapq.heappop(heap)

        parent = Node(
            frequency=left_frequency + right_frequency,
            left=left_node,
            right=right_node,
        )
        heapq.heappush(heap, (parent.frequency, next(unique_id), parent))

    root = heapq.heappop(heap)[2]

    def print_codes(node, code):
        if node.left is None and node.right is None:
            # A single-character input gets code '0' instead of an empty code.
            print(f"{node.character} : {code or '0'}")
            return

        if node.left is not None:
            print_codes(node.left, code + "0")
        if node.right is not None:
            print_codes(node.right, code + "1")

    print("\nHuffman codes:")
    print_codes(root, "")
