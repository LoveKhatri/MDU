# Basic R data structures

# Vector
v <- c("AI", "ML", "R", "Python")
print("Vector:")
print(v)

# List
l <- list(name="Love", roll=2211078, subjects=v)
print("\nList:")
print(l)

# Matrix
m <- matrix(c(85, 92, 88, 90), nrow=2, ncol=2)
print("\nMatrix:")
print(m)

# Array
a <- array(1:8, dim=c(2,2,2))
print("\nArray:")
print(a)

# Data Frame
df <- data.frame(
    Name=c("Love", "Rahul"),
    Score=c(92, 88)
)
print("\nData Frame:")
print(df)