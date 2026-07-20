import sys


class DisjointSetUnion:
    """
    Standard Disjoint Set Union (DSU) data structure with path compression and union by size.
    Used to efficiently group prompts into connected components.
    """

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Path compression for efficiency
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        # Union by size to keep the tree shallow
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.size[root_a] < self.size[root_b]:
                root_a, root_b = root_b, root_a
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]


def main() -> None:
    """
    Solves Task C: Context Enrichment.
    Groups prompts that share at least one word and finds:
    1. Total number of contexts.
    2. Number of unique words in the largest context.

    Complexity: O(W * alpha(N)) time, where W is the total number of word
    occurrences across all prompts and alpha is the inverse Ackermann
    function from DSU union/find with path compression and union by size.
    Space: O(N + W) for the DSU arrays and the word-to-prompt map.
    """
    # Read all input at once for speed
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return

    current_line = 0
    try:
        num_prompts = int(input_lines[current_line].strip())
        current_line += 1
    except (ValueError, IndexError):
        return

    dsu = DisjointSetUnion(num_prompts)

    # Map words to the index of the first prompt that contains them
    word_to_prompt_map: dict[str, int] = {}

    # Store all unique words found in each prompt
    unique_words_in_prompts = []

    for i in range(num_prompts):
        try:
            word_count = int(input_lines[current_line].strip())
            current_line += 1
            prompt_text = input_lines[current_line].strip()
            current_line += 1
            words = set(prompt_text.split())
        except (ValueError, IndexError):
            words = set()

        for word in words:
            if word not in word_to_prompt_map:
                word_to_prompt_map[word] = i
            else:
                # If the word was seen before, join the current prompt with that prompt's group
                dsu.union(i, word_to_prompt_map[word])

    # Count unique words for each component (context)
    # The 'owner' of each word in word_to_prompt_map belongs to some DSU component
    component_word_count: dict[int, int] = {}
    for word, prompt_idx in word_to_prompt_map.items():
        root = dsu.find(prompt_idx)
        component_word_count[root] = component_word_count.get(root, 0) + 1

    # Count total number of unique contexts (components)
    unique_contexts = set()
    for i in range(num_prompts):
        unique_contexts.add(dsu.find(i))

    num_contexts = len(unique_contexts)

    # Find the largest context size
    max_context_size = 0
    if component_word_count:
        max_context_size = max(component_word_count.values())

    print(f"{num_contexts} {max_context_size}")


if __name__ == "__main__":
    main()
