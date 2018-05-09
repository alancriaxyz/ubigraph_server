import xmlrpclib
import time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph;

G.clear()

n = 16 

G.set_vertex_style_attribute(0, "color", "#2EFFFF")
G.set_edge_style_attribute(0, "color", "#ffff00")

def idx(i,j,n):
  return i*n + j;

# Create a graph
for i in range(0,n):
  for j in range(0,n):
    G.new_vertex_w_id(idx(i,j,n))

# Make some edges
for i in range(0,n):
  for j in range(0,n):
    if i != n-1:
      G.new_edge(idx(i,j,n), idx(i+1,j,n))
    if j != n-1:
      G.new_edge(idx(i,j,n), idx(i,j+1,n))

time.sleep(3)

# Turn it into a cylinder
for i in range(0,n):
  G.new_edge(idx(i,n-1,n), idx(i,0,n))

time.sleep(3)

# Turn it into a torus
for j in range(0,n):
  G.new_edge(idx(n-1,j,n), idx(0,j,n))

time.sleep(3)

# Delete the vertices
for i in range(0,n):
  for j in range(0,n):
    G.remove_vertex(idx(i,j,n))

