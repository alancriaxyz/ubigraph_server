import xmlrpclib
import random

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph;

G.clear()

# Edges are splines by default
G.set_edge_style_attribute(0, "spline", "true")

# Set default vertex style
G.set_vertex_style_attribute(0, "shape", "sphere")
G.set_vertex_style_attribute(0, "color", "#ffff00")

# Draw a random graph
n = 40
for i in range(0,n):
  G.new_vertex_w_id(i)
  G.set_vertex_attribute(i, "color", str(i))

# Make the zero vertex big
G.set_vertex_attribute(0, "size", "5.0")

# Make a dashed line style
dashed = G.new_edge_style(0)
G.set_edge_style_attribute(dashed, "stroke", "dashed")
G.set_edge_style_attribute(dashed, "width", "2.0")

for i in range(0,n):
  for j in range(i+1,n):
    if random.random() < 4.0/n:
      e = G.new_edge(i,j)
      G.change_edge_style(e, dashed)
      G.set_edge_attribute(e, "color", str(i))

# Make edges from vertex 0 to every other vertex
for k in range(1,n):
  G.new_edge(0,k)

