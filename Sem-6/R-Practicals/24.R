# Practical 24: Working with Factors in R

# Create student data with categorical variables
student_names <- c("Love", "Rahul", "Priya", "Love", "Amit")
departments <- c("CSE", "IT", "CSE", "CSE", "IT")
grades <- c("A", "B", "A", "A+", "B+")
semester <- rep("6th", length(student_names))

# Convert to factors
student_factor <- factor(student_names)
dept_factor <- factor(departments)
grade_factor <- factor(grades, levels = c("A+", "A", "B+", "B"), ordered = TRUE)
sem_factor <- factor(semester)

# Display information about each factor
cat("Student Analysis using Factors\n")
cat("----------------------------\n")

# Display student name factor
cat("\n1. Student Names:\n")
cat("Unique students:", length(levels(student_factor)), "\n")
cat("Frequency of each student:\n")
print(table(student_factor))

# Display department factor
cat("\n2. Department Distribution:\n")
cat("Available departments:", paste(levels(dept_factor), collapse = ", "), "\n")
dept_freq <- table(dept_factor)
cat("Students per department:\n")
print(dept_freq)

# Display grade factor
cat("\n3. Grade Distribution:\n")
cat("Grade levels (ordered):", paste(levels(grade_factor), collapse = " > "), "\n")
cat("Grade frequencies:\n")
print(table(grade_factor))

# Create a summary data frame
summary_df <- data.frame(
    Name = student_names,
    Department = departments,
    Grade = grades,
    Semester = semester
)

# Display structured summary
cat("\n4. Complete Student Summary:\n")
print(summary_df)

# Check factor properties
cat("\nFactor Properties:\n")
cat("Is 'grade_factor' ordered?:", is.ordered(grade_factor), "\n")
cat("Is 'dept_factor' ordered?:", is.ordered(dept_factor), "\n")
