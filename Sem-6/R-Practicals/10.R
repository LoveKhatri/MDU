# Data frame operations
df <- data.frame(
    Name = c("Love", "Rahul", "Priya"),
    AI = c(85, 82, 88),
    ML = c(92, 85, 89)
)

# Print data frame
print(df)

# Basic analysis
print(mean(df$AI))     # mean of AI scores
print(max(df$ML))      # max ML score
print(subset(df, AI == max(AI)))  # student with highest AI score