import pandas as pd
import numpy as np

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

# Create DataFrame
df = pd.DataFrame(students)

# Extract scores as NumPy array
scores = df["score"].values

# Calculate statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev_score = np.std(scores)

# Add above_average column
df["above_average"] = df["score"] > mean_score

# Print results
print("Mean:", mean_score)
print("Median:", median_score)
print("Standard Deviation:", std_dev_score)
print("\nFinal DataFrame:")
print(df)
