import xmlrpclib

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

x = G.new_vertex()
y = G.new_vertex()
e1 = G.new_edge(x,y)

G.set_vertex_attribute(x, "label", "This is x")

G.set_vertex_attribute(y, "color", "#ffff00")
G.set_vertex_attribute(y, "shape", "dodecahedron")
G.set_vertex_attribute(y, "size", "2.0")

#G.set_edge_attribute(e1, "arrow", "true")

tinyred = G.new_vertex_style(0)
greenedge = G.new_edge_style(0)

G.set_edge_style_attribute(greenedge, "color", "#00ff00")
G.set_edge_style_attribute(greenedge, "strength", "4.0")

for j in range(1,11):
  a = G.new_vertex()
  G.change_vertex_style(a,tinyred)
  G.set_vertex_attribute(a, "label", str(j))
  ya = G.new_edge(y,a)
  G.change_edge_style(ya, greenedge)

G.set_vertex_style_attribute(tinyred, "color", "#800000")
G.set_vertex_style_attribute(tinyred, "size", "0.2")
G.set_vertex_style_attribute(tinyred, "shape", "sphere")

G.set_edge_style_attribute(greenedge, "color", "#00ff00")
G.set_edge_style_attribute(greenedge, "strength", "4.0")

