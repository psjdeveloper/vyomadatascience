import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"C:\Users\praso\vyomadatascience\module02\titanic.csv")
print(data.head())
print(data["Age"].mean())
print(data["Age"].mode())
print(data["Age"].median())
