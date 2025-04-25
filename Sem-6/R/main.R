data <- read.csv("weight-height.csv")

set.seed(42)

split_index <- floor(0.7 * nrow(data))
train_data <- data[1:split_index, ]
test_data <- data[(split_index + 1):nrow(data), ]

plot(train_data$Height, train_data$Weight,
     main = "Height vs Weight (Training Data)",
     xlab = "Height (inches)",
     ylab = "Weight (pounds)",
     pch = 20,
     col = "blue")

model <- lm(Weight ~ Height, data = train_data)

abline(model, col = "red", lwd = 2)

m <- coef(model)[2]
c <- coef(model)[1]

cat("Slope (m):", m, "\n")
cat("Intercept (c):", c, "\n")

predicted_weights <- predict(model, newdata = test_data)

predicted <- head(data.frame(
  Height = test_data$Height,
  Actual_Weight = test_data$Weight,
  Predicted_Weight = predicted_weights
))

print(predicted)