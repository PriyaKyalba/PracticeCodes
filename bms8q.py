# Write a program to print the pattern given below using loop.
# For n = 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()