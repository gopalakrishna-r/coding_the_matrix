from plotting import plot
from image import *

L= [2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j ,2.5+1j, 2.75+1j, 3+1j,3.25 +1j]

plot(L)
I= color2gray(file2image('img01.png'))
r = len(I)
c = len(I[0])
M = [x + y*1j for x in range(c) for y in range(r) if I[r-y-1][x] <120]
plot(M, max(r,c), 1)
