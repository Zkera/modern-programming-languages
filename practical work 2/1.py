import pandas as pd

data = pd.read_csv("practical work 2\\wind_dataset.csv")
print("Максимум:")
print(data.max(numeric_only=True))
print("Минимум:")
print(data.min(numeric_only=True))
print("Среднее:")
print(data.mean(numeric_only=True))
