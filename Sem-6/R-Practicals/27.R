# Practical 27: Linear Regression Analysis

# Simple linear regression
x <- c(85, 78, 90, 82, 88)  # Data Science scores
y <- c(88, 80, 91, 84, 89)  # ML scores

# Perform regression
model <- lm(y ~ x)

# Plot the data and regression line
plot(x, y, main = "Linear Regression", 
     xlab = "Data Science", ylab = "Machine Learning")
abline(model, col = "red")

# Print model summary
print(summary(model))