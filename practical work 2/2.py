import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("practical work 2\\wind_dataset.csv")

maxes = data.max(numeric_only=True) # тут меняй метод

names = list(maxes.keys())
print(names)

x_pos = np.arange(len(names))

values = maxes.values
print(values)

plt.bar(x_pos, values, alpha=0.5)
plt.xticks(x_pos, names)
plt.ylabel("Значения")
plt.title("Максимумы") # тут название


plt.show()