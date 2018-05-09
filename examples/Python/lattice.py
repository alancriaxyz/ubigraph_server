import xmlrpclib

def R(x,y):
  return (y%x) == 0

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

n = 128

G.set_vertex_style_attribute(0, "shape", "none")
G.set_edge_style_attribute(0, "oriented", "true")

# Draw the lcd/gcd lattice
for j in range(2,n+1):
  G.new_vertex_w_id(j)
  G.set_vertex_attribute(j, "label", str(j))
  prime = True
  for i in range(2,j):
    if R(i,j):
      prime = False
      okay = True
      for k in range(i+1,j):
        if R(i,k) and R(k,j):
          okay = False
      if okay:
        G.new_edge(i,j)

  if prime:
    if (2*j > n):
      G.remove_vertex(j)
    else:
      G.set_vertex_attribute(j, "fontsize", "18")
      G.set_vertex_attribute(j, "fontcolor", "#E63434")
  else:
    G.set_vertex_attribute(j, "fontcolor", "#a0a0a0")

