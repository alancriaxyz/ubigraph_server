import xmlrpclib
server = xmlrpclib.Server('http://127.0.0.1:20738/RPC2')
G = server.ubigraph
G.clear()
x = G.new_vertex()
y = G.new_vertex()
G.new_edge(x,y)
G.set_vertex_attribute(x, 'color', '#ff0000')
G.set_vertex_attribute(y, 'shape', 'torus')
G.set_vertex_attribute(y, 'color', '#ffff40')
G.set_vertex_attribute(x, 'label', 'This is red')

