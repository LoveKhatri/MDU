import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Create a customized line plot
plt.plot(x, y1, marker='o', linestyle='--', color='blue', label='Series 1')
plt.plot(x, y2, marker='s', linestyle='-', color='red', label='Series 2')

# Customizing the plot
plt.title('Customized Line Plot', fontsize=14, fontweight='bold')
plt.xlabel('X-axis (Custom)', fontsize=12)
plt.ylabel('Y-axis (Custom)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(color='gray', linestyle=':', linewidth=0.5)  # Custom gridlines

# Show the plot
plt.show()
