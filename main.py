import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create a folder for generated charts
Path("images").mkdir(exist_ok=True)

# Sample student data
data = {
    "Name": ["Aarav", "Priya", "Rahul", "Neha", "Karan"],
    "Maths": [85, 92, 65, 78, 55],
    "Science": [90, 88, 72, 84, 60],
    "English": [78, 95, 70, 82, 58],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate total marks and percentages
subjects = ["Maths", "Science", "English"]

df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = (df["Total"] / 300 * 100).round(2)

# Assign performance categories
def classify_performance(percentage):
    if percentage >= 80:
        return "Excellent"
    elif percentage >= 60:
        return "Good"
    else:
        return "Needs Improvement"

df["Performance"] = df["Percentage"].apply(
    classify_performance
)

# Display the results
print("\nSTUDENT PERFORMANCE ANALYSIS")
print("=" * 65)
print(df.to_string(index=False))

# Calculate class statistics
print("\nCLASS STATISTICS")
print("=" * 65)
print(f"Number of students: {len(df)}")
print(f"Class average: {df['Percentage'].mean():.2f}%")
print(f"Highest percentage: {df['Percentage'].max():.2f}%")
print(f"Lowest percentage: {df['Percentage'].min():.2f}%")

# Save results as a CSV file
df.to_csv("student_results.csv", index=False)
print("\nResults saved to student_results.csv")

# Create a student performance chart
plt.figure(figsize=(10, 6))

plt.bar(df["Name"], df["Percentage"])

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Percentage (%)")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.tight_layout()
plt.savefig("images/performance_chart.png", dpi=150)

print("Chart saved to images/performance_chart.png")

plt.show()