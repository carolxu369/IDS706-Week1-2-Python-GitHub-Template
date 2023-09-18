"""This module contains functions for data analysis using Pandas."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILE_PATH = 'grade.xlsx'
df = pd.read_excel(FILE_PATH)

mean = df['grade'].mean()
median = df['grade'].median()
std_dev = df['grade'].std()

plt.figure(figsize=(10, 6))
plt.hist(df['grade'], bins=20, color='skyblue')
plt.title('Distribution of Grades')
plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.boxplot(df['grade'])
plt.title('Box Plot of Grades')
plt.ylabel('Grade')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(df['grade'], shade=True, color='skyblue')
plt.title('Kernel Density Estimation (KDE) of Grades')
plt.xlabel('Grade')
plt.ylabel('Density')
plt.grid(True)
plt.show()

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
