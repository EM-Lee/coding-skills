### calculate sum of squared integers from 1 to n
### using for loop
def sum_sq(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i**2
    return s

def sum_sq2(n):
    s = 0
    for i in range(1, n + 1):
        s = s + pow(i, 2)
    return s

print(sum_sq(2))
print(sum_sq(5))
print(sum_sq(10))
print()
print(sum_sq2(2))
print(sum_sq2(5))
print(sum_sq2(10))
