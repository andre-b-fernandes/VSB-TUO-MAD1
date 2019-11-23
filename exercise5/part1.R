if (!require("igraph")) 
  install.packages("igraph")
library(igraph) # verze 1.0.1

df <- read.csv("KarateClub.csv", header = F, sep = ';', dec = ',')

g1 <- graph_from_data_frame(d = df, directed = F)

# Diameter
diam <- get_diameter(g1, directed=F)
diam_as_vector <- as.vector(diam)

print("Diameter: ")
diam

# Floyd Warshall Algorithm 
floyd <- function(dataFrame){
  adj_matrix <- matrix(data = Inf , nrow = max(df[1]), ncol = max(df[1]))
  for (row in 1:nrow(dataFrame)) {
     node1 <- dataFrame[row,1]
     node2 <- dataFrame[row,2]
     adj_matrix[node1,node2] <- 1
  }

  for(index in 1:nrow(adj_matrix)){
    adj_matrix[index,index] <- 0
  }
  
  for (k in 1:nrow(adj_matrix)) {
     for (i in 1:nrow(adj_matrix)) {
        for (j in 1:nrow(adj_matrix)) {
            dist1 <- adj_matrix[i,j]
            dist2 <- adj_matrix[i,k]
            dist3 <- adj_matrix[k,j]
            if (dist1 > dist2 + dist3) {
               adj_matrix[i,j] <- dist2 + dist3
            }
        }
     }
  }
  return(adj_matrix)
}

min_distance_between_nodes = floyd(df)

print("Mininum distance between all pair of vertexes: ")
as.data.frame(min_distance_between_nodes)

# Mean distance

m_distance_graph = mean_distance(g1)

print("Mean distance of the Graph: ")
m_distance_graph

mean_distance_for_each_vertex <- function(min_adj_matrix){
    mean_distances = c(1:nrow(min_adj_matrix))
    for (k in 1:nrow(min_adj_matrix)) {
        row = min_adj_matrix[k,]
        filtered_row = row[!is.na(row) & !is.infinite(row)]
        mean_distances[k] <- mean(filtered_row)
    }
    return(mean_distances)
}

mean_distances = mean_distance_for_each_vertex(min_distance_between_nodes)

print("Mean distance of each vertex: ")
as.data.frame(mean_distances)

# Frequency of distances
frequency_table = table(min_distance_between_nodes)

df_frequency_table <- as.data.frame(frequency_table)

print("Frequency Table: ")
df_frequency_table

calculate_data_for_histogram <- function(df_freq){
    data = c()
    for (k in 1:nrow(df_freq)) {
        data <- c(data, as.character(rep(df_freq[k,1], df_freq[k,2]))) 
    }
    return(as.numeric(data))
}

data <- calculate_data_for_histogram(df_frequency_table)
hist(data, col="red", border="gold", main="Frequency of distances", xlab="Distances")