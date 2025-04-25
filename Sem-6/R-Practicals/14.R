# Variable scope
name <- "Love"  # Global variable

demo_scope <- function() {
    age <<- 20  # Global assignment
    local_var <- "Local"  # Local variable
    print(name)  # Access global
    print(local_var)
}

demo_scope()
print(age)  # Access global variable created in function