import time
import ubigraph

ubigraph.ubigraph_clear()

n = 10

def idx(i,j,k,n):
  return i*n*n + j*n + k

# Create a cube graph
for i in range(0,n):
  for j in range(0,n):
    for k in range(0,n):
      ubigraph.ubigraph_new_vertex_w_id(idx(i,j,k,n))
      if i > 0:
        ubigraph.ubigraph_new_edge(idx(i,j,k,n), idx(i-1,j,k,n))
      if j > 0:
        ubigraph.ubigraph_new_edge(idx(i,j,k,n), idx(i,j-1,k,n))
      if k > 0:
        ubigraph.ubigraph_new_edge(idx(i,j,k,n), idx(i,j,k-1,n))

