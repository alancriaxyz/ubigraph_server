import xmlrpclib

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)

server.ubigraph.clear()

# Create a graph
for i in range(0,10):
    server.ubigraph.new_vertex_w_id(i)

# Make some edges
for i in range(0,10):
    server.ubigraph.new_edge(i, (i+1)%10)

