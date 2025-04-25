# Handling missing values
data <- data.frame(
    Name = c("Love", "Rahul", "Priya"),
    Score = c(92, NA, 88)
)

# Check NA values
print(is.na(data))

# Remove NA values
clean_data <- na.omit(data)
print(clean_data)
