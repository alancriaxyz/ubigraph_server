import xmlrpclib
import time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

# Set default edge style
G.set_edge_style_attribute(0, "oriented", "true")
G.set_edge_style_attribute(0, "color", "#C5892F")

# Default vertex style
G.set_vertex_style_attribute(0, "shape", "none")

# Vertex style for leaves
leaf = G.new_vertex_style(0)
G.set_vertex_style_attribute(leaf, "color", "#80219C")
G.set_vertex_style_attribute(leaf, "shape", "sphere")
G.set_vertex_style_attribute(leaf, "size", "3.0")

# Recursive tree construction
def subtree(parent,n):
  v = G.new_vertex()
  e = G.new_edge(parent,v)
  G.set_edge_attribute(e, "width", str(1.0 + n))

  if (n > 0):
    for j in range(0,2):
      v2 = subtree(v,n-1)
  else: 
    G.change_vertex_style(v, leaf)
    time.sleep(0.02)
  return v

# Make a root vertex and build the tree
root = G.new_vertex()
x = subtree(root,8)

