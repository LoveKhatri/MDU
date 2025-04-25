# Practical 21: Exploring R's Built-in Statistical Functions

# Student's semester marks in different subjects
subjects <- c("Data Science", "Machine Learning", "Web Development")
marks <- c(85, 92, 88)  # Modified marks for variation

# Create a header with student info
cat("Statistical Analysis of Academic Performance\n")
cat("Student Name:", "Love", "\n")
cat("Roll No:", "2211078", "\n")
cat("\nSubject-wise Marks:\n")
for(i in 1:length(subjects)) {
    cat(sprintf("%-20s: %d\n", subjects[i], marks[i]))
}

# Calculate and display various statistics
cat("\nStatistical Measures:\n")
cat("-------------------------\n")
cat(sprintf("Total Marks      : %d\n", sum(marks)))
cat(sprintf("Average Score    : %.2f\n", mean(marks)))
cat(sprintf("Highest Mark     : %d\n", max(marks)))
cat(sprintf("Lowest Mark      : %d\n", min(marks)))
cat(sprintf("Mark Range       : %d\n", max(marks) - min(marks)))
cat(sprintf("Standard Dev     : %.2f\n", sd(marks)))
cat(sprintf("Median Score     : %.2f\n", median(marks)))
