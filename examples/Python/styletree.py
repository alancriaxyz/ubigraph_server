import xmlrpclib
import time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

G.set_edge_style_attribute(0, "oriented", "true")
G.set_edge_style_attribute(0, "arrow", "true")

style0 = 0
style1 = G.new_vertex_style(style0)
style2 = G.new_vertex_style(style0)
G.set_vertex_style_attribute(style0, "color", "#0000ff")

G.set_vertex_style_attribute(style2, "shape", "cube")
G.set_vertex_style_attribute(style2, "color", "#00ff00")

style3 = G.new_vertex_style(style2)
style4 = G.new_vertex_style(style2)

G.set_vertex_style_attribute(style0, "label", "style 0")
G.set_vertex_style_attribute(style1, "label", "style 1")
G.set_vertex_style_attribute(style2, "label", "style 2")
G.set_vertex_style_attribute(style3, "label", "style 3")
G.set_vertex_style_attribute(style4, "label", "style 4")

v0 = G.new_vertex()
v1 = G.new_vertex()
G.new_edge(v0,v1)
v2 = G.new_vertex()
G.new_edge(v0,v2)
v3 = G.new_vertex()
G.new_edge(v2,v3)
v4 = G.new_vertex()
G.new_edge(v2,v4)

G.change_vertex_style(v0,style0)
G.change_vertex_style(v1,style1)
G.change_vertex_style(v2,style2)
G.change_vertex_style(v3,style3)
G.change_vertex_style(v4,style4)

time.sleep(2)

G.set_vertex_style_attribute(style0, "color", "#ff0000")
G.set_vertex_style_attribute(style1, "shape", "octahedron")

time.sleep(2)
G.set_vertex_style_attribute(style0, "size", "3.0")

time.sleep(2)
G.set_vertex_style_attribute(style0, "size", "1.0")

