# DAA Programs — Simple Python Explanations

This folder contains beginner-friendly Python versions of the six Java programs. Each `.py` file can be run independently with Python 3.

## 1. Fibonacci using a loop — `fibonacci_iterative.py`

**Idea:** Each Fibonacci number is the sum of the previous two numbers. The sequence starts with `0, 1, 1, 2, 3, 5, ...`.

**How it works:**
1. Start with `a = 0` and `b = 1`.
2. Print `a`.
3. Move the values forward: `a` becomes `b`, and `b` becomes the old `a + b`.
4. Repeat this for the requested number of terms.

**Important line:** `a, b = b, a + b` updates both values together using their old values.

**Example:** For `n = 6`, output is `0 1 1 2 3 5`.

**Complexity:** Time `O(n)`; extra space `O(1)`. This is the efficient version for generating a sequence.

## 2. Fibonacci using recursion — `fibonacci_recursive.py`

**Idea:** Define the function in terms of smaller versions of itself: `fib(n) = fib(n-1) + fib(n-2)`.

**Base cases:** `fibonacci(0)` returns `0` and `fibonacci(1)` returns `1`. These stop the recursive calls.

**How it works:** To calculate a term such as `fibonacci(4)`, the function calls `fibonacci(3)` and `fibonacci(2)`, which make more calls until they reach the base cases. The main loop calls the function for each index from `0` to `n-1`.

**Complexity:** The direct recursive method takes exponential time (roughly `O(2^n)` for one term) because it repeats many calculations. Its recursion stack can use `O(n)` space. It is useful for understanding recursion, but it is not suitable for large inputs.

## 3. Fractional Knapsack — `fractional_knapsack.py`

**Problem:** Select items to maximize profit without exceeding a weight capacity. In this version, an item can be split into a fraction.

**Greedy idea:** Prefer the item with the highest profit per unit of weight.

**How it works:**
1. For each item, calculate `ratio = profit / weight`.
2. Sort items by this ratio from highest to lowest.
3. If the entire item fits, take it and add its full profit.
4. Otherwise, take the fraction that fits: `fraction = remaining_capacity / item_weight`.
5. Add `profit * fraction` and stop because the bag is full.

**Why greedy works here:** Items are divisible, so taking the best profit-per-weight available first gives an optimal solution.

**Complexity:** Sorting takes `O(n log n)` time; storing items takes `O(n)` space.

**Do not confuse it with 0/1 Knapsack:** Fractional Knapsack permits partial items; 0/1 Knapsack does not.

## 4. 0/1 Knapsack — `zero_one_knapsack.py`

**Problem:** Each item must either be taken completely or not taken. Items cannot be split.

**Technique:** Dynamic programming (DP), which stores answers to smaller subproblems so they do not need to be recalculated.

**Meaning of the table:** `dp[i][w]` is the maximum profit possible using the first `i` items and a capacity of `w`.

For each item and each capacity:
- If the item is too heavy, copy the result from the previous row: `dp[i - 1][w]`.
- If it fits, compare two choices:
  - **Skip it:** `dp[i - 1][w]`
  - **Take it:** `profit[i] + dp[i - 1][w - weight[i]]`
- Store the larger value.

The final answer is `dp[n][capacity]`.

**Why use the previous row when taking an item?** This ensures the same item cannot be selected more than once.

**Complexity:** Time `O(nW)` and space `O(nW)`, where `n` is the number of items and `W` is the integer capacity. This is called pseudo-polynomial time because it depends on the numeric capacity.

## 5. Huffman Encoding — `huffman_encoding.py`

**Purpose:** Build variable-length binary codes that give shorter codes to more frequent characters, often reducing the total encoded size.

**Key data structure:** A min-priority queue (Python's `heapq`) that always removes the node with the smallest frequency.

**How it works:**
1. Create one leaf node per character, containing its frequency.
2. Remove the two nodes with the smallest frequencies.
3. Join them under a new parent node whose frequency is their sum.
4. Put the parent back in the queue.
5. Repeat until only one node remains; it is the root of the Huffman tree.
6. Traverse the tree: going left adds `0`; going right adds `1`. The code at a leaf belongs to that character.

**Why the unique ID exists in the Python heap:** When frequencies tie, it gives the heap a safe way to order entries without trying to compare `Node` objects. Equal-frequency cases can produce different but equally valid Huffman codes.

**Complexity:** `O(n log n)` time and `O(n)` space for `n` distinct characters.

## 6. N-Queens — `n_queens.py`

**Problem:** Place `N` queens on an `N × N` chessboard so that no two queens attack each other. Queens attack along rows, columns, and diagonals.

**Technique:** Backtracking.

**How it works:**
1. Place one queen in the current row.
2. Before placing it, `is_safe(row, col)` checks the column and both upward diagonals. Only earlier rows need checking because queens are placed from top to bottom.
3. If the position is safe, place the queen and recursively solve the next row.
4. If the later rows cannot be solved, remove the queen (`board[row][col] = 0`) and try the next column. This undo step is called **backtracking**.
5. Reaching `row == N` means every row has a queen and a solution is found.

**Output:** `Q` represents a queen and `.` represents an empty square. The program prints one solution, not every possible solution.

**Complexity:** Exponential search; `O(N!)` is a common rough description. The board uses `O(N^2)` space, plus recursion stack space.

## How to run the programs

1. Install Python 3 if it is not already installed.
2. Open a terminal or command prompt in this folder.
3. Run one file at a time, for example:

```bash
python fibonacci_iterative.py
python fibonacci_recursive.py
python fractional_knapsack.py
python zero_one_knapsack.py
python huffman_encoding.py
python n_queens.py
```

On some systems, use `python3` instead of `python`.

## Quick comparison

| Program | Main technique | Time complexity | Main use |
|---|---|---|---|
| Fibonacci iterative | Loop | `O(n)` | Generate Fibonacci numbers efficiently |
| Fibonacci recursive | Recursion | Roughly `O(2^n)` per term | Learn recursive definitions |
| Fractional Knapsack | Greedy + sorting | `O(n log n)` | Maximize profit when items can be split |
| 0/1 Knapsack | Dynamic programming | `O(nW)` | Maximize profit when items cannot be split |
| Huffman Encoding | Greedy + min-heap + tree | `O(n log n)` | Create frequency-based binary codes |
| N-Queens | Backtracking | Exponential, roughly `O(N!)` | Search for a non-attacking queen arrangement |

`W` is the knapsack capacity. For 0/1 Knapsack, weights and capacity are integers in this implementation.
