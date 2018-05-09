import xmlrpclib

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

style1 = G.new_vertex_style(0)
style2 = G.new_vertex_style(style1)

# Create a graph
for i in range(0,10):
    G.new_vertex_w_id(i)
    G.change_vertex_style(i,style1)
    G.new_vertex_w_id(i+10)
    G.change_vertex_style(i+10,style2)

# Make some edges
for i in range(0,10):
    G.new_edge(i, (i+1)%10)
    G.new_edge(10+i, 10+(i+1)%10)
    G.new_edge(i, 10+i)

G.set_vertex_style_attribute(style1, "color", "#ff0000")
G.set_vertex_style_attribute(style2, "shape", "sphere")
G.set_vertex_style_attribute(style1, "shape", "torus")

G.set_vertex_attribute(0, "label", "vertex 0")

