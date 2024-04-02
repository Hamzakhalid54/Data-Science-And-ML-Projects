zz <- read.table("lettersdata.txt") 
zz <- as.matrix(zz)


plot(zz, main="Scatterplot of the Data", xlab="Dimension 1", ylab="Dimension 2", col=4, pch=19)






k_value <- 5
set.seed(42) 
km_result <- kmeans(zz, centers=k_value)

plot(zz, col=km_result$cluster, main="K-Means Clustering Results", xlab="Dimension 1", ylab="Dimension 2", pch=19)
points(km_result$centers, col=1:k_value, pch=8, cex=2)










k_values <- 2:20
totwss_values <- numeric(length(k_values))

for (i in seq_along(k_values)) {
  set.seed(42) # Ensure reproducibility
  km_result <- kmeans(zz, centers=k_values[i])
  totwss_values[i] <- km_result$tot.withinss
}

plot(k_values, totwss_values, type="b", col="blue", main="TOTWSS vs Number of Clusters", xlab="Number of Clusters", ylab="TOTWSS", pch=19)





#2
# Load necessary library
library(kernlab)

# Perform spectral clustering
set.seed(42) # Ensure reproducibility
spcl <- specc(zz, centers=4) # Using 4 clusters as specified

# Convert clustering results to a numeric vector for plotting
spcl_clusters <- as.numeric(spcl)

# Plot the results of spectral clustering
plot(zz, col=spcl_clusters, main="Spectral Clustering Results", xlab="Dimension 1", ylab="Dimension 2", pch=19)




















