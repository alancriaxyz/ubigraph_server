
import xmlrpclib

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2';
server = xmlrpclib.Server(server_url);
G = server.ubigraph

G.clear()

y = G.new_vertex()
G.set_vertex_attribute(y, "shape", "none")

def dovertex():
  x = G.new_vertex()
  G.new_edge(y,x)
  G.set_vertex_attribute(x, "shapedetail", "100")
  G.set_vertex_attribute(x, "color", "#ff0000")
  return x

def dofont(family,size):
  x = dovertex()
  G.set_vertex_attribute(x, "fontfamily", family)
  G.set_vertex_attribute(x, "fontsize", size)
  G.set_vertex_attribute(x, "label", family + " " + str(size) + "pt")

#  raw_input()

dofont("Helvetica", "10")
dofont("Helvetica", "12")
dofont("Helvetica", "18")
dofont("Times Roman", "10")
dofont("Times Roman", "24")

x = dovertex()
G.set_vertex_attribute(x, "fontcolor", "#ffff00");
G.set_vertex_attribute(x, "label", "Yellow");
G.set_vertex_attribute(x, "fontsize", "24");

