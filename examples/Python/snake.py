import xmlrpclib
import time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph;

G.clear()

n = 1000

G.set_vertex_style_attribute(0, "color", "#12AF31")
G.set_vertex_style_attribute(0, "shape", "icosahedron")

# Create a graph
for i in range(0,n):
  G.new_vertex_w_id(i)
  if ((i%10) == 0):
    G.set_vertex_attribute(i, "label", str(i))
  if (i > 0):
    G.new_edge(i,i-1)
  if (i >= 50):
    G.remove_vertex(i-50)
  time.sleep(0.01)
  if ((i%100) == 0):
    time.sleep(0.5)

