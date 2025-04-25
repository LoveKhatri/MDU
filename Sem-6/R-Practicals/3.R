# Statistical measures
marks <- c(85, 78, 91, 63, 78, 85, 88)

# Find mode
mode <- names(sort(table(marks), decreasing=TRUE)[1])

cat("Min:", min(marks), "\n")
cat("Max:", max(marks), "\n")
cat("Mean:", mean(marks), "\n")
cat("Median:", median(marks), "\n")
cat("Mode:", mode, "\n")