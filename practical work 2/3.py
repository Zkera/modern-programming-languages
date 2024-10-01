import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def GraphMax():
    path = text_field.get()
    data = pd.read_csv(path)

    maxes = data.max(numeric_only=True) 

    names = list(maxes.keys())
    print(names)

    x_pos = np.arange(len(names))

    values = maxes.values
    print(values)

    plt.bar(x_pos, values, alpha=0.5)
    plt.xticks(x_pos, names)
    plt.ylabel("Значения")
    plt.title("Максимумы")


    plt.show()
def GraphMin():
    path = text_field.get()
    data = pd.read_csv(path)

    maxes = data.min(numeric_only=True) 

    names = list(maxes.keys())
    print(names)

    x_pos = np.arange(len(names))

    values = maxes.values
    print(values)

    plt.bar(x_pos, values, alpha=0.5)
    plt.xticks(x_pos, names)
    plt.ylabel("Значения")
    plt.title("Минимум") 

    plt.gca().invert_yaxis()
    plt.show()
def GraphMean():
    path = text_field.get()
    data = pd.read_csv(path)

    maxes = data.mean(numeric_only=True)

    names = list(maxes.keys())
    print(names)

    x_pos = np.arange(len(names))

    values = maxes.values
    print(values)

    plt.bar(x_pos, values, alpha=0.5)
    plt.xticks(x_pos, names)
    plt.ylabel("Значения")
    plt.title("Среднее") 


    plt.show()

#practical work 2\\wind_dataset.csv
window = tk.Tk()
label = tk.Label(text="Путь")
text_field = tk.Entry(width=80)
button_max = tk.Button(text="Максимум", command=GraphMax)
button_min = tk.Button(text="Минимум", command=GraphMin)
button_mean = tk.Button(text="Среднее", command=GraphMean)

label.pack()
text_field.pack()
button_max.pack() 
button_min.pack() 
button_mean.pack()
text_field.insert(0, "practical work 2\\wind_dataset.csv")

window.mainloop()

