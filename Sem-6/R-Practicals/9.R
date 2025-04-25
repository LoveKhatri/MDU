# Matrix operations
m <- matrix(c(85, 88, 92, 82, 87, 90), nrow=2, byrow=TRUE)
colnames(m) <- c("AI", "ML", "R")
rownames(m) <- c("Love", "Rahul")

# Calculate sums and means
print(rowSums(m))   # sum by row
print(colSums(m))   # sum by column
print(rowMeans(m))  # mean by row
print(colMeans(m))  # mean by column
