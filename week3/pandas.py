import numpy as np
import pandas as pd

plaat = np.zeros(shape=(5, 6))

bestelling_array = np.array([[2, 2], [1, 1], [3, 5]])


bestelling = np.ones(shape=bestelling_array[0,:])

result = np.zeros_like(plaat)
x_offset = 0  # 0 would be what you wanted
y_offset = 0  # 0 in your case
result[x_offset:bestelling.shape[0]+x_offset,y_offset:bestelling.shape[1]+y_offset] = bestelling

print(result)




