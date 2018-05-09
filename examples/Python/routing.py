import xmlrpclib, time, random

# Number of dimensions for hypercube
dim = 6

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2';
server = xmlrpclib.Server(server_url);
G = server.ubigraph

G.clear()

# While we are building the graph, make everything invisible.
G.set_vertex_style_attribute(0, "visible", "false")
G.set_edge_style_attribute(0, "visible", "false")

# Default vertex styles
G.set_vertex_style_attribute(0, "shape", "sphere")
G.set_vertex_style_attribute(0, "color", "#F4FF85")
G.set_vertex_style_attribute(0, "size", "0.25")

activeVertex = G.new_vertex_style(0)
G.set_vertex_style_attribute(activeVertex, "color", "#FF4B30")

# Convert integer to binary, code by Antti Kaihola
bstr_pos = lambda n: n>0 and bstr_pos(n>>1)+str(n&1) or ''
bstr_nonneg = lambda n: n>0 and bstr_nonneg(n>>1).lstrip('0')+str(n&1) or '0'
bstr_sgn = lambda n: n<0 and '-'+binarystr(-n) or n and bstr_sgn(n>>1).lstrip('0')+str(n&1) or '0'
bstr = lambda n, l=16: n<0 and binarystr((2L<<l)+n) or n and bstr(n>>1).lstrip('0')+str(n&1) or '0'

r = pow(2,dim)

for i in range(0,r):
  G.new_vertex_w_id(i)
  G.set_vertex_attribute(i, "label", bstr(i))

for i in range(0,r):
  for j in range(0,dim):
    k = pow(2,j)
    if i & k == 0:
      e = i*r + (i+k)
      G.new_edge_w_id(e, i, i+k)
      G.set_edge_attribute(e, "strength", str(pow(1.0/(j+1),1.5)))

# Reveal the graph
G.set_vertex_style_attribute(0, "visible", "true")
G.set_edge_style_attribute(0, "visible", "true")

def animateArrow(e, reverse):
  pos = 0.0
  if reverse:
    pos = 1.0
  G.set_edge_attribute(e, "arrow_position", str(pos))
  G.set_edge_attribute(e, "arrow_reverse", str(reverse))
  G.set_edge_attribute(e, "arrow", "true")
  for i in range(0,20):
    a = i / 19.0
    if reverse:
      a = 1.0 - a
    G.set_edge_attribute(e, "arrow_position", str(a))
    time.sleep(0.05)
  G.set_edge_attribute(e, "arrow", "false")

pos = 0
for n in range(0,10):
  next_pos = random.randrange(0,r)
  G.change_vertex_style(pos, activeVertex)
  G.change_vertex_style(next_pos, activeVertex)
  v_from = pos
  for j in range(0,dim):
    k = pow(2,j)
    diff = (next_pos & k) - (pos & k)  
    v_to = v_from + diff
    e = v_from*r + v_to
    if v_from > v_to:
      e = v_to*r + v_from

    if diff > 0:
      animateArrow(e, False)
    elif diff < 0:
      animateArrow(e, True)
    v_from = v_to
  G.change_vertex_style(pos, 0)
  time.sleep(0.5)
  pos = next_pos


