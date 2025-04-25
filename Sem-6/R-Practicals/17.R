# While loop to print natural numbers
i <- 1
cat("Natural numbers from 1 to 10:\n")

while (i <= 10) {
    cat(i, ifelse(i < 10, "-> ", "\n"))
    i <- i + 1
}
