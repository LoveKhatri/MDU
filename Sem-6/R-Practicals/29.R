# Logistic regression example

# Define the data
hours <- c(2.5, 5.5, 3.0, 8.0, 1.5)
passed <- c(0, 1, 0, 1, 0)

# Fit logistic model
model <- glm(passed ~ hours, family = binomial)

# Print summary
print(summary(model))

# Make predictions
new_data <- data.frame(hours = c(4, 6))
pred <- predict(model, newdata = new_data)
print(pred)