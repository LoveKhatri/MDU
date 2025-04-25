import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]

# Create histogram
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.show()
