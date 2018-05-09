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
G.set_vertex_attribute(x, "shape", "sphere");
G.set_vertex_attribute(x, "shapedetail", "40");
G.set_vertex_attribute(x, "label", "shapedetail=40");
G.set_vertex_attribute(y, "shape", "sphere");
G.set_vertex_attribute(y, "shapedetail", "10");
G.set_vertex_attribute(y, "label", "shapedetail=10");
G.set_vertex_attribute(z, "shape", "sphere");
G.set_vertex_attribute(z, "shapedetail", "5");
G.set_vertex_attribute(z, "label", "shapedetail=5");
