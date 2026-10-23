"""0/1 Knapsack using dynamic programming."""

n = int(input("Enter number of items: "))
weights = [0]  # Index 0 is a dummy value to make item numbering easier.
profits = [0]

for i in range(1, n + 1):
    weight = int(input(f"Enter weight of item {i}: "))
    profit = int(input(f"Enter profit of item {i}: "))
    if weight < 0:
        raise ValueError("Item weight cannot be negative.")
    weights.append(weight)
    profits.append(profit)

capacity = int(input("Enter knapsack capacity: "))
if capacity < 0:
    raise ValueError("Capacity cannot be negative.")

# dp[i][w] = best profit using the first i items with capacity w.
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for current_capacity in range(capacity + 1):
        # Option 1: do not take this item.
        dp[i][current_capacity] = dp[i - 1][current_capacity]

        # Option 2: take this item, if it fits.
        if weights[i] <= current_capacity:
            take_profit = profits[i] + dp[i - 1][current_capacity - weights[i]]
            dp[i][current_capacity] = max(
                dp[i][current_capacity], take_profit
            )

print(f"\nMaximum profit = {dp[n][capacity]}")
