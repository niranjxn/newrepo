
#####################
# 7. List Operations
#####################
# Grocery Store Inventory Example

fruits = ["apple", "banana"]
vegetables = ["carrot", "potato"]
inventory = fruits + vegetables
print(f"Store inventory: {inventory}")

prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Cheap items (first 3): {prices[:3]}")
print(f"Expensive items (last 3): {prices[-3:]}")
print(f"Medium range prices: {prices[3:7]}")
print(f"Alternate price tags: {prices[::2]}")

discounted_prices = [p * 0.9 for p in prices[:5]]
even_priced_items = [p for p in prices if p % 2 == 0]

print(f"Discounted prices: {discounted_prices}")
print(f"Even-priced items: {even_priced_items}")

