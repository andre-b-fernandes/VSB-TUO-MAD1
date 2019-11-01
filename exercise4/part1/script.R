df<-read.csv("../KarateClub.csv", header = F, sep = ";", dec = ",")
df

if (!require("igraph")) 
  install.packages("igraph")
library(igraph) # verze 1.0.1

g1 <- graph_from_data_frame(d = df, directed = F)

diameter(g1, directed = F) # diameter == longest shortest path, value
diam <- get_diameter(g1, directed = F) # vertices forming the first found path of a given length
as.vector(diam) # from an igraph class object to make a  vector
# plot
vcol <- rep("lightblue", vcount(g1))
vcol[diam] <- "gold"
ecol <- rep("black", ecount(g1)) #
ecol[E(g1, path = diam)] <- "red"

plot(g1, vertex.color = vcol, edge.color = ecol, edge.arrow.mode = 0)


mean_distance(g1, directed = F) 
# the distance matrix between all pairs of nodes of the graph
A <- distances(g1) 

# the path between the selected pair of vertices
path1 <- shortest_paths(g1, from = V(g1)["1"], to = V(g1)["27"], output = "both") # "both path" nodes and edges
ecol <- rep("black", ecount(g1))
ecol[unlist(path1$epath)] <- "red"

# We generate a width of edges forming the path
ew <- rep(1, ecount(g1))
ew[unlist(path1$epath)] <- 2

# We generate the color of the path vertexes
vcol <- rep("lightblue", vcount(g1))
vcol[unlist(path1$vpath)] <- "gold"
plot(g1, vertex.color = vcol, edge.color = ecol, edge.width = ew, edge.arrow.mode = 0)

# counted as 1 / sum (length of all paths from node i), caution the result is not sorted by id of node
centr <- closeness(g1, mode = "all", weights = NA) 

# counted as (n-1) / sum (length of all paths from node i), beware result is not sorted by id of node
centr_clo(g1, mode = "all", normalized = F)

# computed by our own function as n / sum (length of all paths from vertex i)
fce_clos <- function(x)
{
  cc <- numeric(34)
  souc <- 0
  for(i in 1: nrow(x))
  {
    
    cc[i] = 34 / (sum(A[i,]))
  }
  return(cc)
}

fce_clos(A)

plot(x = as.numeric(names(centr)), y = as.numeric(centr), xlab = "Degree", ylab = "Closeness")
names(which(centr == min(centr))) # find the node with the lowest centrality
names(which(centr == max(centr))) # highest


# own function for determining the frequency of individual path lengths (from the lower triangular matrix)
fce <- function(x)
{
  v <- numeric(max(x) + 1)
  for(i in 1: nrow(x))
  {
    for(j in 1 : i)  
    {
      v[A[i,j]+1] = v[A[i,j]+1]+1
    }
  }
  return(v)
}
# we could still modify it to avoid elements on the diagonal, that is, paths of length 0 ....

# we plot the frequency, we get it by our function
barplot(as.numeric(fce(A)), names.arg = c(0:max(A))) 

floyd <- function(dataFrame){
  adjecency_matrix <- matrix(data = .Machine$integer.max , nrow = max(df[1]), ncol = max(df[1]))
  for (row in 1:nrow(dataFrame)) {
     node1 <- dataFrame[row,1]
     node2 <- dataFrame[row,2]
     adjecency_matrix[node1,node2] <- 1
  }

  for(index in 1:nrow(adjecency_matrix)){
    adjecency_matrix[index,index] <- 0
  }
  
  for (k in 1:nrow(adjecency_matrix)) {
     for (i in 1:nrow(adjecency_matrix)) {
        for (j in 1:nrow(adjecency_matrix)) {
            dist1 <- adjecency_matrix[i,j]
            dist2 <- adjecency_matrix[i,k]
            dist3 <- adjecency_matrix[k,j]
            if (dist1 > dist2 + dist3) {
               adjecency_matrix[i,j] <- dist2 + dist3
            }
        }
     }
  }

  return(adjecency_matrix)
}