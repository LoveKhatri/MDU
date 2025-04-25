# Practical 25: Advanced Statistical Analysis in R

# Student performance data across different subjects
scores <- c(85, 88, 92, 78, 91)

cat("Percentiles:\n")
cat("25th:", quantile(scores, 0.25), "\n")
cat("50th (Median):", quantile(scores, 0.5), "\n")
cat("75th:", quantile(scores, 0.75), "\n")

cat("\nVariance:", var(scores), "\n")
cat("Standard Deviation:", sd(scores), "\n")
