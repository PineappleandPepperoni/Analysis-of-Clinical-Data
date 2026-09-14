import matplotlib.pyplot as plt

# Data
Diets = [
    "Plant-based",
    "Flexitarian",
    "Vegeterian/vegan",
    "Mediterranean",
    "DASH"
]

# Proportion of people on these diets
Proportion = [
    11.8,
    7.4,
    6.1,
    5.8,
    5.5
]

# Create a chart
plt.bar(Diets, Proportion)

# Add labels
plt.xlabel("Types of Diets")
plt.ylabel("Proportion of Diets (%)")
plt.title("American Diets in 2022")

# Make the x-axis easier to read
plt.xticks(rotation=45, ha="right")

# Display the chart
plt.tight_layout()
plt.show()