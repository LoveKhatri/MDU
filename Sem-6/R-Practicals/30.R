# Practical 30: Advanced Data Visualization in R

# Load required libraries
library(ggplot2)

# Basic plot types
marks <- c(85, 92, 88, 90, 87)
subjects <- c("DS", "ML", "Web", "AI", "R")

# Line plot
plot(marks, type = "l", main = "Line Plot")

# Scatter plot
plot(1:5, marks, main = "Scatter Plot", pch = 19)

# Bar plot
barplot(marks, names.arg = subjects, main = "Bar Plot")

# Pie chart
pie(marks, labels = subjects, main = "Pie Chart")

# Histogram
hist(c(marks, marks+2, marks-2), main = "Histogram")