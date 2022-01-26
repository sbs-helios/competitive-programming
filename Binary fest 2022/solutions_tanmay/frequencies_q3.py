from collections import defaultdict

n = int(input())
s = input()

freq_dict = defaultdict(int)

for ch in s:
    freq_dict[ch] += 1

items = list(freq_dict.items())

for i in range(len(items)):
    items[i] = tuple(reversed(items[i]))

for elem in sorted(items):
    print(elem[1] * elem[0], end="")

print()
