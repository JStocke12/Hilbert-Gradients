from PIL import Image
from numpy import array
from numpy import vectorize
from colorsys import hsv_to_rgb as hsv

Hilbert_Array = [[0]]

def bit_prepend(h, n):
    s = h[-1][0].bit_length()
    return [[(n << s) | e for e in l] for l in h]

def expand(h):
    return [sum(i, []) for i in list(zip(list(map(list, zip(*h))),bit_prepend(h,1)))+list(zip(list(map(lambda l: list(l)[::-1], zip(*bit_prepend(h,3))))[::-1],bit_prepend(h,2)))]

for i in range(10):
    Hilbert_Array = expand(Hilbert_Array)

img = Image.new('HSV', (len(Hilbert_Array),len(Hilbert_Array)))

px = img.load()

for i in range(len(Hilbert_Array)):
    for j in range(len(Hilbert_Array)):
        px[i,j] = (Hilbert_Array[i][j]%256, 255, 255)

img.convert(mode='RGB').save("image.png")

Image.open("image.png").show()
