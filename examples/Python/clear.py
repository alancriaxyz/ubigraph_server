import xmlrpclib
import time

# Omit from run_all.sh

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph;

G.clear()
