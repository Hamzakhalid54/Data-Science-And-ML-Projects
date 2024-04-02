#b
mu0 <- 150
sigma0 <- 20
sigma <- 10
xbar <- 160

# Function to calculate posterior mean and standard deviation
posterior_params <- function(n) {
  mu_prime <- (mu0 / sigma0^2 + n * xbar / sigma^2) / (1 / sigma0^2 + n / sigma^2)
  sigma_prime_squared <- 1 / (1 / sigma0^2 + n / sigma^2)
  return(c(mu_prime, sqrt(sigma_prime_squared)))
}

# Calculations
n10 <- posterior_params(10)
n100 <- posterior_params(100)
n1 <- posterior_params((1))

print(paste("n=1: mu'=", n1[1], ", sigma'=", n1[2]))
print(paste("n=10: mu'=", n10[1], ", sigma'=", n10[2]))
print(paste("n=100: mu'=", n100[1], ", sigma'=", n100[2]))



#c
# Define the prior function piecewise
prior_function <- function(theta) {
  ifelse(theta <= 150, 1/45000 * theta - 1/900, 
         ifelse(theta <= 200, -1/90000 * theta + 7/1800, 
                -1/30000 * theta - 1/120 + 251/120))
}

# Create a sequence of theta values
theta_values <- seq(50, 250, length.out = 1000)
prior_values <- Vectorize(prior_function)(theta_values)

# Normalize the prior (to ensure it integrates to 1 over its domain)
prior_values <- prior_values / sum(prior_values) * length(theta_values) / (max(theta_values) - min(theta_values))

# Plot the prior distribution
library(ggplot2)
ggplot(data.frame(theta = theta_values, Prior = prior_values), aes(x = theta, y = Prior)) +
  geom_line(color = "blue") +
  labs(title = "Prior Distribution of Height", x = expression(theta), y = "Density") +
  theme_minimal()




# Hypothetical Likelihood (assuming it could be Gaussian with mean = 160, sd = 10)
likelihood_function <- function(theta) {
  dnorm(theta, mean = 160, sd = 10)
}

likelihood_values <- likelihood_function(theta_values)

# Plot the likelihood distribution
ggplot(data.frame(theta = theta_values, Likelihood = likelihood_values), aes(x = theta, y = Likelihood)) +
  geom_line(color = "red") +
  labs(title = "Likelihood Distribution of Height", x = expression(theta), y = "Density") +
  theme_minimal()

