
import xmlrpclib

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

y = G.new_vertex()
G.set_vertex_attribute(y, "shape", "none")

def doshape(s):
  x = G.new_vertex()
  G.new_edge(y,x)
  G.set_vertex_attribute(x, "shapedetail", "100")
  G.set_vertex_attribute(x, "color", "#ff7f5e")
  G.set_vertex_attribute(x, "shape", s)
  G.set_vertex_attribute(x, "label", s)

doshape("cone")
doshape("sphere")
doshape("torus")
doshape("cube")
doshape("octahedron")
doshape("tetrahedron")
doshape("dodecahedron")
doshape("icosahedron")

