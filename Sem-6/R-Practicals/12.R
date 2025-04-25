# Write data frame to CSV
student <- data.frame(
    Name = "Love",
    Roll = 2211078,
    AI = 85,
    ML = 92
)

# Write to CSV
write.csv(student, "student.csv", row.names = FALSE)