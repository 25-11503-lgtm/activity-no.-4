sum_num = 0

for num in range(1, 51):
    if num % 3 == 0:
        continue
    print(num, end=" ")
    sum_num += num

print(f"\nSum: {sum_num}")
