import matplotlib.pyplot as plt

# Sample data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [35, 30, 20, 15]

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Pie Chart Example')
plt.show()
