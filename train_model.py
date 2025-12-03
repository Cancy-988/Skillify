import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv(r"C:\Users\cancy\Downloads\synthetic_dataset1.csv")

X = df[['aptitude', 'dsa', 'dbms', 'os']]   
y = df['job_ready']                        


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)


with open("job_ready_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'job_ready_model.pkl'")

