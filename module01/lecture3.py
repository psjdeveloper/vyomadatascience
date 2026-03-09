import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

a = np.array([i for i in range(10)])
# two ways to calculate mean 
# 1. manually 
manual_mean = sum(a)/ len(a)
# 2. using numpy 
numpy_mean = np.mean(a)

print(f"Manual mean: {manual_mean}")    
print(f"Numpy mean: {numpy_mean}")