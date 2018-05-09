import xmlrpclib
import time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph;

G.clear()

n = 10

def idx(i,j,k,n):
  return i*n*n + j*n + k

# Create a cube graph
for i in range(0,n):
  for j in range(0,n):
    for k in range(0,n):
      G.new_vertex_w_id(idx(i,j,k,n))
      if i > 0:
        G.new_edge(idx(i,j,k,n), idx(i-1,j,k,n))
      if j > 0:
        G.new_edge(idx(i,j,k,n), idx(i,j-1,k,n))
      if k > 0:
        G.new_edge(idx(i,j,k,n), idx(i,j,k-1,n))

