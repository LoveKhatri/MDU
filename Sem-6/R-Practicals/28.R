# Multiple linear regression
data <- data.frame(
    DS = c(85, 78, 90, 82, 88),
    Web = c(82, 75, 88, 80, 85),
    ML = c(88, 80, 91, 84, 89)
)

# Fit model
model <- lm(ML ~ DS + Web, data = data)

# Print summary
print(summary(model))