# Data manipulation with dplyr
library(dplyr)

data <- data.frame(
    name = c("Love", "Rahul", "Priya"),
    ml = c(92, 85, 88)
)

result <- data %>%
    rename(Name = name, ML = ml) %>%
    filter(ML > 85)

print(result)
