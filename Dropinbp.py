import matplotlib.pyplot as plt

# Data
diets = [
    "Plant-based",
    "Flexitarian",
    "Vegetarian,vegan",
    "Mediterranean",
    "DASH"
]

# Drop in blood pressure
blood_pressure = [
    5,
    5.5,
    4.5,
    1.5,
    1
]

# Create a chart
plt.bar(diets, blood_pressure)

# Add labels
plt.xlabel("Types of diets")
plt.ylabel("Estimated mean drop in blood pressure (mmHg)")
plt.title("Effect of diet on drop in blood pressure")

# Make labels easier to read
plt.xticks(rotation=45, ha="right")

# Display the chart
plt.tight_layout()
plt.show()
