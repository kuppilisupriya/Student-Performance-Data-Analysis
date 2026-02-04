import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# Data Cleaning
df.dropna(inplace=True)

# Exploratory Data Analysis
print(df.describe())

# Visualization
plt.figure()
plt.bar(df["Student_ID"], df["Math_Score"])
plt.xlabel("Student ID")
plt.ylabel("Math Score")
plt.title("Math Performance of Students")
plt.show()
