import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv("students.csv")

X = data[['cgpa','skills','projects','internships']]
y = data['placed']

model = LogisticRegression()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully")
