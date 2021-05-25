Hilbert_Array = [[[0],[1]],[[3],[2]]]

def expand(h):
    return list(zip(h,h))+list(zip(h,h))

print(expand(Hilbert_Array))
