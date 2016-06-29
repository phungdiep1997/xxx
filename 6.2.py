li = ['meo', 'bo', 'ga', 'cho', 'chim', 'lon']
output = list((li[i], li[j]) for i in range(len(li)) for j in range(len(li)) if i % 2 == 0 and j == i + 1)
print(output)