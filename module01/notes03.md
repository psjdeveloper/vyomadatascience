

# 📘 Lecture 3 — The Art of Collecting Data

By **Vyoma Youth Society**

In this lecture, we will discuss **how data is collected** and perform a small practical example using Python.

In the previous lectures, we discussed:

* what data really is
* why uncertainty exists in data

But before moving deeper into statistics and machine learning, we must understand something very basic:

> **Where does data come from?**

Data does not appear magically.
Collecting data is a **skill and a process**.

So the first question we should ask is:

> **Where can we collect data from?**

Before continuing, pause for a moment and write down a few places where you think data can be collected.

---

## Collection of Data

Before we start working with statistics or building models, we must first have data to work with.

Data collection is the **foundation of data science**.
Without data, analysis is impossible.

When we think about collecting data, there are generally two main types of sources.

---

## Types of Data Sources

### 1️⃣ Primary Sources

Primary data is the data that **you collect yourself**.

This usually involves first-hand methods such as:

* surveys
* interviews
* experiments
* observations

In primary data collection, you design the method and gather the data directly.

Example:
If you conduct a survey asking students about their study hours, the data you collect is **primary data**.

---

### 2️⃣ Secondary Sources

Secondary data is data that has already been collected by someone else.

Instead of collecting it yourself, you **use existing datasets**.

Examples include:

* public datasets
* research papers
* government statistics
* online databases

Using secondary data is very common in data science because many organizations publish large datasets.

---

For now, we will only introduce these concepts.
Later in this course, we will have a **full module dedicated to data collection**, where we will study these methods in much greater detail.

---

# Practical Section

In the last two lectures we focused mainly on theory.
So today we will do a **small practical exercise**.

Our goal is simple:

> Compare the **manual calculation of the mean** with the **mean calculated by a Python library**.

This helps us understand that libraries are simply **implementations of mathematical formulas**.

---

## Python Practical

First, create a Python file and write the following code.

```python
import numpy as np

a = np.array([i for i in range(10)])

# 1. Manual calculation
manual_mean = sum(a) / len(a)

# 2. Using NumPy
numpy_mean = np.mean(a)

print(f"Manual mean: {manual_mean}")
print(f"Numpy mean: {numpy_mean}")
```

---

## Understanding What Happened

Before understanding the code, we should understand what **mean** really is.

The **mean** is simply the **average value** of a dataset.

The formula is:

[
Mean = \frac{\text{Sum of all values}}{\text{Number of values}}
]

In the program:

* `sum(a)` adds all numbers in the dataset
* `len(a)` gives the number of elements
* `sum(a) / len(a)` calculates the mean manually

Then we use the NumPy function:

```
np.mean(a)
```

This function performs the same calculation internally.

When you run the code, both methods give the same result:

**4.5**

This shows that library functions are simply **automated versions of mathematical formulas**.

---

## What This Practical Teaches Us

1️⃣ Data must first be collected before analysis.
2️⃣ Statistics is built on simple mathematical ideas.
3️⃣ Programming libraries automate these calculations.

Understanding the **mathematics behind the libraries** is an important goal of this initiative.

---
