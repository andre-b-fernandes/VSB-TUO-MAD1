if (!require("igraph")) 
  install.packages("igraph")
library(igraph) # verze 1.0.1

df <- read.csv("KarateClub.csv", header = F, sep = ';', dec = ',')

g1 <- graph_from_data_frame(d = df, directed = F)

#Local
local_clustering_coefficients <- transitivity(g1, type = "local")
print("Local clustering coefficients: ")
as.data.frame(local_clustering_coefficients)

#Global
print("Graph transitivity: ")
average_transivity <- transitivity(g1, type = "average")
average_transivity