import xmlrpclib
import time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

x = G.new_vertex()
y = G.new_vertex()
z = G.new_vertex()
G.new_edge(x,y)
G.new_edge(y,z)

mystyle = G.new_vertex_style(0);

G.set_vertex_style_attribute(mystyle, "color", "#ff0000")
G.change_vertex_style(x, mystyle)

G.set_vertex_style_attribute(0, "shape", "torus")

