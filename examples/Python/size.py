import xmlrpclib

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2';
server = xmlrpclib.Server(server_url);
G = server.ubigraph

G.clear()

x = G.new_vertex()
y = G.new_vertex() 
z = G.new_vertex()
G.new_edge(x,y)
G.new_edge(y,z)
G.set_vertex_style_attribute(0, "shapedetail", "40");
G.set_vertex_style_attribute(0, "shape", "torus");
G.set_vertex_style_attribute(0, "color", "#ffc65c");

G.set_vertex_attribute(y, "label", "size=1.0");

G.set_vertex_attribute(x, "size", "2.0");
G.set_vertex_attribute(x, "label", "size=2.0");

G.set_vertex_attribute(z, "size", "0.5");
G.set_vertex_attribute(z, "label", "size=0.5");

