import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate a large dataset
np.random.seed(42)
rows = 100000
data = {
    'X': np.random.randint(1, 100, rows),
    'Y': np.random.randint(1, 100, rows),
    'Value': np.random.randn(rows)
}
df = pd.DataFrame(data)

# Aggregate data to reduce clutter
heatmap_data = df.pivot_table(index='Y', columns='X', values='Value', aggfunc='mean')

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='coolwarm', cbar=True)
plt.title('Heatmap of Large Dataset', fontsize=16)
plt.xlabel('X-axis (Aggregated)', fontsize=12)
plt.ylabel('Y-axis (Aggregated)', fontsize=12)
plt.show()
