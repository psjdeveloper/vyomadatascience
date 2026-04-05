

# 📊 Lecture 1 — Central Tendency of Data

### *Vyoma Data Science Initiative | Module 2: Statistics*

---

## 🧠 Introduction

In any dataset, we often face a simple question:

> Can we represent all this data using a single number?

Whether it’s exam scores, income levels, or age distributions — we try to **summarize complexity into simplicity**.

This idea leads us to **central tendency**.

---

## 📌 What is Central Tendency?

Central tendency refers to the **representative value** of a dataset — the point around which the data tends to cluster.

It helps answer:

* What is typical?
* Where does the data concentrate?
* What does this dataset “look like” overall?

---

## 🔢 Measures of Central Tendency

### 1️⃣ Mean (Average)

[
\text{Mean} = \frac{\sum x_i}{n}
]

* Represents the **balance point** of the dataset
* Highly sensitive to **outliers**

---

### 2️⃣ Median (Middle Value)

* The **middle value** after sorting data
* If even number of values → average of two middle values

👉 More **robust** than mean in real-world datasets

---

### 3️⃣ Mode (Most Frequent Value)

* The value that appears **most often**
* Useful for both **numerical and categorical data**

---

## ⚠️ When Averages Mislead

Consider:

```
2, 3, 4, 5, 100
```

* Mean = 22.8 ❌
* Median = 4 ✅

👉 The mean is distorted by an extreme value.

---

### 🧭 Insight

> A single number cannot always capture reality.
> The choice of measure defines the “truth” you see.

---

## 🧪 Practical Implementation (Python)

Using the **Titanic dataset**, we analyze the **Age** column.

### 🔹 Code

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\praso\vyomadatascience\module02\titanic.csv")

print(data.head())

print("Mean Age:", data["Age"].mean())
print("Mode Age:", data["Age"].mode())
print("Median Age:", data["Age"].median())
```

---

## 📊 Optional Visualization

```python
sns.histplot(data["Age"].dropna(), kde=True)
plt.title("Age Distribution (Titanic Dataset)")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
```

---

## 📂 Dataset Reference

You can download the Titanic dataset from:

* Titanic Dataset
* Official Kaggle link: [https://www.kaggle.com/datasets/yasserh/titanic-dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

(You can place it in your project folder: `module02/titanic.csv`)

---

## 💻 GitHub Repo 
Download the github repo of our course from here :
[https://github.com/psjdeveloper/vyomadatascience](https://github.com/psjdeveloper/vyomadatascience)
---


---

## 🧭 Final Reflection

Central tendency is not just about computing mean, median, or mode.

It is about understanding:

* How data behaves
* How summaries can distort reality
* And how **interpretation matters more than calculation**

---

## ✍️ Closing Line

> Data does not speak for itself.
> The way we summarize it decides what it says.

---

