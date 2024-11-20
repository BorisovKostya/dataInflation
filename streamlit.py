import streamlit as st
import numpy as np
import pandas as pd 
import scipy.stats
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
import statistics
st.title("Инфляция в России")
if st.button("Click me!"):
    st.write(":pig:")
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
    st.dataframe(df)
    plt.xticks(np.arange(1985,2026,5))
    plt.yticks(np.arange(0,3100,100))
    plt.plot(x,y)
    st.pyplot()



plt.show()