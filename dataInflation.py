import numpy as np
import pandas as pd 
import scipy.stats
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
import statistics
df = pd.read_csv("1.txt",delimiter='\t')
df2=df
x = df["Год"]
df2.pop("Год")
df2.pop("Всего")
y = df2
plt.figure(figsize=(10,6))
plt.title("Инфляция в России ")
plt.xlabel("Year") 
plt.ylabel("inflation") 
#plt.hist(df)
plt.plot(x,y)
plt.show()
