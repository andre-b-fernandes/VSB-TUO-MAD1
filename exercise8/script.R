# 1. Generate a random graph
if (!require("igraph")) 
  install.packages("igraph")
library(igraph) # verze 1.0.1


## Graphs
random_graph <- erdos.renyi.game(550, 550*200, type="gnm",  directed = FALSE)
regular_graph <- sample_k_regular(550, 200, directed = FALSE, multiple = FALSE)
ba_graph <- sample_pa(550)
small_world_graph <- sample_smallworld(1, 550, 100, 0.05)

## Degrees
random_graph_degree <- degree(random_graph)
regular_graph_degree <- degree(regular_graph)
ba_graph_degree <- degree(ba_graph)
small_world_graph_degree <- degree(small_world_graph)

## Degree distribution
degree_distribution_random_graph <- degree_distribution(random_graph)
degree_distribution_regular_graph <- degree_distribution(regular_graph)
degree_distribution_ba_graph <- degree_distribution(ba_graph)
degree_distribution_small_world_graph <- degree_distribution(small_world_graph)

