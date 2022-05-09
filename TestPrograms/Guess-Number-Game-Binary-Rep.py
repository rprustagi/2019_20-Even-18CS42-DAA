import numpy as np
import pandas as pd

maxpower = 7
gmr = [None] * maxpower
count=2**(maxpower - 1)

# approach 1
for i in range(maxpower):
    x=[j for j in range(2**maxpower) if j & 2**i == 2**i]
    gmr[i] = pd.DataFrame(np.array(x).reshape(8,8))
    gmr[i].to_excel('Card' + str(i+1) + 'xlsx')
    print(gmr[i])

# approach 2 (optimal)
gmro = [[]] * maxpower
for i in range(maxpower):
    x = []
    j = 2 ** i
    while j < 2 ** maxpower:
        for l in range(j, j + 2**i):
            x.append(l)
        j = j + 2*2**i
    gmro[i] = pd.DataFrame(np.array(x).reshape(2**((maxpower -1) // 2), 2**(maxpower // 2)))
    print(gmro[i])

