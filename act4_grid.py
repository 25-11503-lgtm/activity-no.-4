# Input validation
while True:
    n = int(input("Size: "))
    if 1 <= n <= 10:
        break
    print("Please enter a number between 1‑10")

# Nested loop multiplication table
for row in range(1, n + 1):
    for col in range(1, n + 1):
        value = row * col
        print(f"{value:4d}", end="")
    print()
