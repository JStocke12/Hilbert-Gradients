Hilbert_Array = [[0]]

def bit_prepend(h, n):
    s = h[-1][0].bit_length()
    return [[(n << s) | e for e in l] for l in h]

def expand(h):
    return [sum(i, []) for i in list(zip(list(map(list, zip(*h))),bit_prepend(h,1)))+list(zip(list(map(lambda l: list(l)[::-1], zip(*bit_prepend(h,3))))[::-1],bit_prepend(h,2)))]

for i in range(4):
    Hilbert_Array = expand(Hilbert_Array)

print(Hilbert_Array)
