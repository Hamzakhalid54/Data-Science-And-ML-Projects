# R code snippet for plotting the prior and posterior distributions
library(ggplot2)

# Function to calculate the density of an inverse-gamma distribution
dinv_gamma <- function(x, shape, scale) {
  return(scale^shape / gamma(shape) * x^(-shape - 1) * exp(-scale / x))
}

# Create a sequence of x values
x_values <- seq(0.01, 20, length.out = 1000)

# Calculate densities for prior and posterior
prior_density <- dinv_gamma(x_values, 0.5, 10)
posterior_density <- dinv_gamma(x_values, 3.5, 56)

# Convert to data frames for ggplot
prior_df <- data.frame(x_values, Density = prior_density)
posterior_df <- data.frame(x_values, Density = posterior_density)

# Plot the distributions
ggplot() +
  geom_line(data = prior_df, aes(x = x_values, y = Density, color = "Prior"), size = 1) +
  geom_line(data = posterior_df, aes(x = x_values, y = Density, color = "Posterior"), size = 1) +
  labs(x = "Dwell Time", y = "Density", title = "Prior and Posterior Distributions") +
  scale_color_manual(values = c("Prior" = "blue", "Posterior" = "red")) +
  theme_minimal()

