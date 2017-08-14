### find the minimum value from a list

def find_min(a):
    n = len(a)
    min_v = [0]

    for i in range(1, n):
        if a[i] < min_v:
            min_v = a[i]
    return min_v

v = [56, 24, 32, 45, 16, 23, 5, 10]

print(find_min(v))
