import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Create Performance Category
avg_score = (
    df["math score"] +
    df["reading score"] +
    df["writing score"]
) / 3

df["performance"] = avg_score.apply(
    lambda x:
    "Poor" if x < 40 else
    "Average" if x < 60 else
    "Good" if x < 80 else
    "Excellent"
)

# Features
X = df.drop(
    ["math score",
     "reading score",
     "writing score",
     "performance"],
    axis=1
)

# Encode categorical columns
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

# Encode target
target_encoder = LabelEncoder()
y = target_encoder.fit_transform(df["performance"])

# Train Model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(
    model,
    open("models/model.pkl", "wb")
)

pickle.dump(
    target_encoder,
    open("models/encoder.pkl", "wb")
)

print("Model Trained Successfully")