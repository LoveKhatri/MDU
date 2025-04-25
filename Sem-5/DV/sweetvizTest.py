import sweetvizTest as sv
import pandas as pd

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Operations']
}
df = pd.DataFrame(data)

# Create and display Sweetviz report
report = sv.analyze(df)  # Analyze the dataset
report.show_html('sweetviz_report.html')  # Generate an HTML report
