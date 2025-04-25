# Multiplication table
num <- 20
cat("Table of", num, ":\n")

for (i in 1:10) {
    cat(sprintf("%d × %d = %d\n", num, i, num * i))
}