library(dplyr)
library(ggplot2)
library(rstatix)
library(effsize)

# Read the data
data <- read.csv("hbr_maples.csv")

# Test for normality within each group defined by watershed and elevation
normality_results <- data %>%
  group_by(watershed, elevation) %>%
  shapiro_test(stem_dry_mass)

# Print the normality results
print(normality_results)

# Function to calculate effect size for Mann-Whitney U test (Rank-biserial correlation)
calculate_effect_size <- function(x, y) {
  test <- wilcox.test(x, y)
  n1 <- length(x)
  n2 <- length(y)
  effect_size <- (test$statistic - (n1 * (n1 + 1) / 2)) / (n1 * n2)
  return(effect_size)
}

# Perform Mann-Whitney U test for the Reference watershed between Low and Mid elevations
comparison <- data %>%
  filter(watershed == "Reference", elevation %in% c("Low", "Mid"))

mann_whitney <- wilcox.test(stem_dry_mass ~ elevation, data = comparison, exact = FALSE)

# Calculate effect size for Mann-Whitney U test
effect_size <- calculate_effect_size(
  comparison$stem_dry_mass[comparison$elevation == "Low"],
  comparison$stem_dry_mass[comparison$elevation == "Mid"]
)

# Print the test results and effect size
print(mann_whitney)
print(effect_size)

# Create a boxplot for the Reference watershed comparing Low and Mid elevations
ggplot(comparison, aes(x = elevation, y = stem_dry_mass, color = elevation)) +
  geom_boxplot() +
  labs(title = "Stem Dry Mass by Elevation within Reference Watershed",
       x = "Elevation",
       y = "Stem Dry Mass") +
  theme_minimal()

# Display the plot
ggsave("stem_dry_mass_comparison.png", width = 10, height = 6, dpi = 300)

