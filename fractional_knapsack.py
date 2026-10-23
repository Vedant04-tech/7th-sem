"""Fractional Knapsack using a greedy strategy."""

n = int(input("Enter number of items: "))
items = []

for i in range(n):
    weight = float(input(f"Enter weight of item {i + 1}: "))
    profit = float(input(f"Enter profit of item {i + 1}: "))

    if weight <= 0:
        raise ValueError("Item weight must be greater than zero.")

    # Store profit per unit of weight along with the item details.
    ratio = profit / weight
    items.append((ratio, weight, profit))

capacity = float(input("Enter knapsack capacity: "))
if capacity < 0:
    raise ValueError("Capacity cannot be negative.")

# Greedy choice: consider the best profit/weight ratio first.
items.sort(reverse=True)
total_profit = 0.0
print("\nSelected items:")

for ratio, weight, profit in items:
    if capacity == 0:
        break

    if weight <= capacity:
        # The whole item fits.
        capacity -= weight
        total_profit += profit
        print(f"Taken completely: weight={weight:g}, profit={profit:g}")
    else:
        # Take only the fraction that fits.
        fraction = capacity / weight
        total_profit += profit * fraction
        print(f"Taken fraction: {fraction:.2f} of an item")
        capacity = 0

print(f"\nMaximum profit = {total_profit:g}")
