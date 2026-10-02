import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("students.csv")

# CGPA vs Placement
plt.figure(figsize=(6,4))
sns.scatterplot(x="cgpa", y="placed", data=data)

plt.title("CGPA vs Placement")
plt.xlabel("CGPA")
plt.ylabel("Placement")

plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x="skills", y="placed", data=data)

plt.title("Skills vs Placement")
plt.xlabel("Skills")
plt.ylabel("Placement")

plt.show()

sns.histplot(data["placed"])
plt.title("Placement Distribution")
plt.show()