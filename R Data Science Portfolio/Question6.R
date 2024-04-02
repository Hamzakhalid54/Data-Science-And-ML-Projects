# Define the total cases and deaths for Florida and Arizona
florida_cases <- 7627999
florida_deaths <- 89075
arizona_cases <- 2486671
arizona_deaths <- 29852

# Define the priors for Florida and Arizona
florida_prior <- c(6000, 500000)
arizona_prior <- c(2700, 200000)

# Calculate the posterior distributions for Florida and Arizona
florida_posterior <- florida_prior + c(florida_deaths, florida_cases - florida_deaths)
arizona_posterior <- arizona_prior + c(arizona_deaths, arizona_cases - arizona_deaths)

# Calculate posterior medians and 95% credible intervals for Florida and Arizona
florida_median <- qbeta(0.5, florida_posterior[1], florida_posterior[2])
florida_credible_interval <- qbeta(c(0.025, 0.975), florida_posterior[1], florida_posterior[2])

arizona_median <- qbeta(0.5, arizona_posterior[1], arizona_posterior[2])
arizona_credible_interval <- qbeta(c(0.025, 0.975), arizona_posterior[1], arizona_posterior[2])

# Create a table-like structure for the results
results_table <- data.frame(
  Location = c("Florida", "Arizona"),
  Total_Cases = c(florida_cases, arizona_cases),
  Total_Deaths = c(florida_deaths, arizona_deaths),
  Posterior_Median = c(florida_median, arizona_median),
  `95%_Credible_Interval_Lower` = c(florida_credible_interval[1], arizona_credible_interval[1]),
  `95%_Credible_Interval_Upper` = c(florida_credible_interval[2], arizona_credible_interval[2])
)

# Print the results table
print(results_table)

# Plot the prior and posterior distributions for Florida
theta <- seq(0, 1, length.out = 1000)
prior_fl <- dbeta(theta, florida_prior[1], florida_prior[2])
posterior_fl <- dbeta(theta, florida_posterior[1], florida_posterior[2])

plot(theta, prior_fl, type = "l", col = "blue", ylim = c(0, max(posterior_fl)), 
     main = "Florida - Prior vs Posterior", xlab = "Fatality Rate", ylab = "Density")
lines(theta, posterior_fl, col = "red")

# Plot the prior and posterior distributions for Arizona
prior_az <- dbeta(theta, arizona_prior[1], arizona_prior[2])
posterior_az <- dbeta(theta, arizona_posterior[1], arizona_posterior[2])

plot(theta, prior_az, type = "l", col = "blue", ylim = c(0, max(posterior_az)), 
     main = "Arizona - Prior vs Posterior", xlab = "Fatality Rate", ylab = "Density")
lines(theta, posterior_az, col = "red")

