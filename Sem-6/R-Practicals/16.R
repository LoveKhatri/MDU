# Switch statement example
course <- "ML"

message <- switch(course,
    "AI" = "You chose Artificial Intelligence",
    "ML" = "You chose Machine Learning",
    "R" = "You chose R Programming",
    "Invalid choice")

cat("Love's selection:", message, "\n")
