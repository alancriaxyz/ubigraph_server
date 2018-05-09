import xmlrpclib, time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2';
server = xmlrpclib.Server(server_url);
G = server.ubigraph

G.clear()

x = G.new_vertex()
y = G.new_vertex()
G.set_vertex_style_attribute(0, "shape", "sphere")
G.set_vertex_style_attribute(0, "color", "#F4FF85")
G.set_vertex_style_attribute(0, "size", "0.25")

e = G.new_edge(x,y)
G.set_edge_attribute(e, "arrow", "true")
G.set_edge_attribute(e, "color", "#FFD4D7")

def animateArrowPosition(e):
  G.set_edge_attribute(e, "arrow_reverse", "false")
  for i in range(0,20):
    a = i/19.0
    G.set_edge_attribute(e, "arrow_position", str(a))
    time.sleep(0.05)
  G.set_edge_attribute(e, "arrow_reverse", "true")
  for i in range(0,20):
    a = 1.0 - i/19.0
    G.set_edge_attribute(e, "arrow_position", str(a))
    time.sleep(0.05)
  G.set_edge_attribute(e, "arrow_reverse", "false")

def animateArrowLength(e):
  G.set_edge_attribute(e, "arrow_position", "0.5")
  for i in range(0,13):
    a = (i+1) / 7.0
    G.set_edge_attribute(e, "arrow_length", str(a))
    time.sleep(0.05)

def animateArrowRadius(e):
  for i in range(0,20):
    a = (i+1) / 10.0
    G.set_edge_attribute(e, "arrow_radius", str(a))
    time.sleep(0.05)

animateArrowPosition(e)
animateArrowLength(e)
animateArrowRadius(e)
G.set_edge_attribute(e, "arrow_radius", "0.5")
G.set_edge_attribute(e, "arrow_length", "1.0")
animateArrowPosition(e)

