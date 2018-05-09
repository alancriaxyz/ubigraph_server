import xmlrpclib

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

y = G.new_vertex()

G.set_vertex_attribute(y, "color", "#ffff00")
G.set_vertex_attribute(y, "shape", "dodecahedron")
G.set_vertex_attribute(y, "size", "2.0")

tinyred = G.new_vertex_style(0)
greenedge = G.new_edge_style(0)

G.set_edge_style_attribute(greenedge, "color", "#00ff00")
G.set_edge_style_attribute(greenedge, "strength", "4.0")

for j in range(1,12):
  G.new_vertex_w_id(100+j)
  G.change_vertex_style(100+j,tinyred)
  ya = G.new_edge_w_id(200+j,y,100+j)

G.set_vertex_style_attribute(tinyred, "color", "#800000")
G.set_vertex_style_attribute(tinyred, "size", "0.2")
G.set_vertex_style_attribute(tinyred, "shape", "sphere")

G.set_edge_style_attribute(greenedge, "color", "#00ff00")
G.set_edge_style_attribute(greenedge, "strength", "4.0")



# Change some edge attributes

G.set_edge_attribute(201, "label", "labelled")
G.set_edge_attribute(202, "color", "#00ff00")
G.set_edge_attribute(202, "label", "green")

G.set_edge_attribute(203, "length", "3.0")
G.set_edge_attribute(203, "label", "length=3.0")

G.set_edge_attribute(204, "width", "2.0")
G.set_edge_attribute(204, "label", "width=2.0")

G.set_edge_attribute(205, "width", "4.0")
G.set_edge_attribute(205, "label", "width=4.0")

G.set_edge_attribute(206, "arrow", "true")
G.set_edge_attribute(206, "label", "arrow=true")

for j in range(1,5):
  e2 = G.new_edge(101, 102)
  G.set_edge_attribute(e2, "spline", "true")
  G.set_edge_attribute(e2, "label", "spline=true")

G.set_edge_attribute(208, "visible", "false")
G.set_vertex_attribute(108, "label", "visible=false")

G.set_edge_attribute(209, "fontsize", "24")
G.set_edge_attribute(209, "label", "fontsize=24")

G.set_edge_attribute(210, "fontcolor", "#ff0000")
G.set_edge_attribute(210, "label", "fontcolor=#ff0000")

G.set_edge_attribute(211, "stroke", "dashed")
G.set_edge_attribute(211, "label", "stroke=dashed")

e2 = G.new_edge(110, 111)
G.set_edge_attribute(e2, "stroke", "dotted")
G.set_edge_attribute(e2, "spline", "true")
G.set_edge_attribute(e2, "label", "stroke=dotted")

