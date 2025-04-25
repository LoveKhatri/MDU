# Practical 20: Factorial Calculator

# Factorial calculator
factorial_fn <- function(n) {
    if (n < 0) return("Error: negative number")
    if (n <= 1) return(1)
    
    result <- 1
    for (i in 2:n) {
        result <- result * i
    }
    return(result)
}

cat("Factorial of 6:", factorial_fn(6), "\n")
