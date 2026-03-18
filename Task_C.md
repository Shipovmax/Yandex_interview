# Task C: Context Enrichment

## Task
You need to "compress" a set of user prompts: group together prompts whose sets of words overlap by at least one word. This grouping is transitive (if prompt A overlaps with B, and B overlaps with C, then A, B, and C are in the same context).

Your goal is to find:
- The total number of resulting contexts.
- The size (number of unique words) of the largest context.

## Input Format
1. The first line contains the integer **N** (1 ≤ N ≤ 1000) — the number of prompts.
2. Then, for each **i = 1..N**, two lines are provided:
   - **Mᵢ** (1 ≤ Mᵢ ≤ 1000) — the number of words in the i-th prompt.
   - A line of **Mᵢ** words (only lowercase Latin letters, length 1..10), separated by spaces.

Note: Repeated words within a single prompt are treated as the same word.

## Output Format
Print two integers separated by a space:
- The number of resulting contexts.
- The size (number of unique words) of the largest context.

## Examples
### Example 1
**Input:**
```
3
4
a four word prompt
2
small prompt
5
unique line with five words
```
**Output:**
```
2 5
```
*Explanation:* The first and second prompts share the word "prompt" and form a context with words {a, four, word, prompt, small} (size 5). The third prompt is isolated and forms its own context {unique, line, with, five, words} (size 5).

### Example 2
**Input:**
```
1
1
a
```
**Output:**
```
1 1
```

### Example 3
**Input:**
```
2
2
a b
2
b c
```
**Output:**
```
1 3
```
*Explanation:* Both prompts share the word "b", forming a single context {a, b, c} (size 3).
