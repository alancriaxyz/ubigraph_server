import xmlrpclib
import time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

x = G.new_vertex()
y = G.new_vertex()

G.set_edge_style_attribute(0, "spline", "true")

G.set_vertex_style_attribute(0, "shape", "sphere")
G.set_vertex_style_attribute(0, "size", "0.3")
G.set_vertex_style_attribute(0, "color", "#FFDB25")

for i in range(0,20):
  G.new_edge(x,y)
  time.sleep(0.4)

