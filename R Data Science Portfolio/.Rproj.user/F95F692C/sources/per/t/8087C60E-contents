# Load the data from the CSV file
the.fulldata <- read.csv("MelbAirportSolarData.csv", header = TRUE, sep = ",")

# Assuming you need to sample the data as per your original instructions
set.seed(123) # Setting a seed for reproducibility
sampled_indices <- sample(1:nrow(the.fulldata), 5000) # Adjust the number of rows if different
my.data <- the.fulldata[sampled_indices, ]

# Convert the data frame to a matrix (Ensure this is done if needed or skip if analysis on dataframe is preferable)
my.data <- as.matrix(my.data)

# Assuming 'Wind speed' is indeed the third column in the sampled data
wind_speed <- as.numeric(my.data[, 3]) # Ensure conversion to numeric in case of matrix type issues

# Generate a histogram for 'Wind speed'
hist(wind_speed, main = "Histogram of Wind Speed", xlab = "Wind Speed (m/s)", col = "lightblue", border = "blue")

# Generate a box plot for 'Wind speed'
boxplot(wind_speed, horizontal = TRUE, main = "Box Plot of Wind Speed", col = "lightgreen")

# Compute a five-number summary for 'Wind speed'
five_num_summary <- fivenum(wind_speed) # Tukey's five number summary
print(five_num_summary)

# Alternatively, use summary for a traditional five-number summary plus mean
summary_windspeed <- summary(wind_speed)
print(summary_windspeed)






#1.3
# Assuming 'Temperature' is the second column and 'Humidity' is the fourth column in your dataset
temperature <- my.data[, 2] # Adjust if necessary
humidity <- my.data[, 4] # Adjust if necessary

# 1. Create a scatterplot for 'Temperature' and 'Humidity'
plot(temperature, humidity, xlab = "Temperature (°C)", ylab = "Humidity (%)", main = "Scatterplot of Temperature vs Humidity")

# 2. Fit a linear regression model to the variables
model <- lm(humidity ~ temperature)

# 3. Plot the regression line on the scatterplot
abline(model, col = "red")

# 4. Write down the linear regression equation
# Intercept and slope (coefficients) of the linear model
intercept <- coef(model)[1]
slope <- coef(model)[2]
cat("The linear regression equation is: Humidity = ", intercept, " + ", slope, "*Temperature\n")

# 5. Compute the correlation coefficient
correlation_coefficient <- cor(temperature, humidity)
cat("Correlation coefficient: ", correlation_coefficient, "\n")

# 6. Compute the coefficient of Determination (R²)
r_squared <- summary(model)$r.squared
cat("Coefficient of Determination (R²): ", r_squared, "\n")










#1.4
# Check the structure of my.data
print(str(my.data))


# Assign column names from the matrix's dimnames attribute
colnames <- attr(my.data, "dimnames")[[2]]

# Create the new variables within my.data, which we will first convert to a data frame
my.data <- data.frame(my.data)

# Now set the names to the columns of the data frame
names(my.data) <- colnames

# Convert 'wind.speed' to km/h from m/s
my.data$WSB <- ifelse(as.numeric(my.data$wind.speed) * 3.6 > 25, "High", "Low")

# Categorize 'ambient.temp' according to specified ranges
my.data$TB <- ifelse(as.numeric(my.data$ambient.temp) > 30, "High",
                     ifelse(as.numeric(my.data$ambient.temp) >= 20, "Moderate", "Low"))

# Categorize 'irradiance' according to specified threshold
my.data$IrrB <- ifelse(as.numeric(my.data$irradiance) > 800, "High", "Low")

# Create the cross table for the new variables
cross_table <- table(my.data$WSB, my.data$TB, my.data$IrrB)

# Print the cross table
print(cross_table)


# Total number of records
total_records <- 137 + 281 + 400 + 4 + 12 + 142 + 2576 + 1180 + 238 + 30

irrb_high_total <- 137 + 281 + 400 + 4 + 12
p_irrb_high <- irrb_high_total / total_records
p_irrb_high

wsb_low_total <- 4 + 12 
p_tb_high_given_wsb_low <- 0 / wsb_low_total
p_tb_high_given_wsb_low

tb_moderate_and_wsb_low_total <- 12 + 30  # Total where TB is moderate and WSB is low
p_irrb_low_given_tb_moderate_and_wsb_low <- 30 / tb_moderate_and_wsb_low_total
p_irrb_low_given_tb_moderate_and_wsb_low


# Probability of TB being high
p_tb_high <- (142 + 137) / total_records
p_tb_high
# Probability of IrrB being low
p_irrb_low <- (142 + 2576 + 1180 + 238 + 30) / total_records
p_irrb_low
# Check for independence
independence_check <- p_tb_high * p_irrb_low == 142 / total_records
independence_check

mutual_exclusivity_check <- (281 == 0)
mutual_exclusivity_check



