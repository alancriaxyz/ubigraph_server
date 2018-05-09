# Omit from run_all.sh
import xmlrpclib
import time
import random

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

G.set_edge_style_attribute(0, "oriented", "true")
G.set_vertex_style_attribute(0, "color", "#ff00ff")
G.set_vertex_style_attribute(0, "shape", "sphere")

root = G.new_vertex()
G.set_vertex_attribute(root, "label", "Doubleclick me")

highlightStyle = G.new_vertex_style(0)
G.set_vertex_style_attribute(highlightStyle, "color", "#ff80ff")
G.set_vertex_style_attribute(highlightStyle, "size", "2.0")

myPort = random.randint(20739,20999)

# Set up a callback for left double-clicks on vertices.
G.set_vertex_style_attribute(0, "callback_left_doubleclick", 
  "http://127.0.0.1:" + str(myPort) + "/vertex_callback")

# Now make an XMLRPC server to handle tha callbacks.
from SimpleXMLRPCServer import SimpleXMLRPCServer

# Create server
server = SimpleXMLRPCServer(("localhost", myPort))
server.register_introspection_functions()

def vertex_callback(v):
  try:
    G.change_vertex_style(v, highlightStyle)
    r = G.new_vertex()
    s = G.new_vertex()
    G.new_edge(v,r)
    G.new_edge(v,s)
    G.set_vertex_attribute(r, "color", str(random.randint(1,1024)))
    G.set_vertex_attribute(s, "color", str(random.randint(1,1024)))

    # Make the vertex we clicked on shrink slowly
    for i in range(1,11):
      time.sleep(0.1)
      G.set_vertex_attribute(v, "size", str(2.0 - i/10.0))
    G.change_vertex_style(v, 0)

    # Get rid of "Doubleclick me" on root, if it's still there
    G.change_vertex_style(root, 0)

  except:
    return -1

  return 0

server.register_function(vertex_callback)

# Run the server's main loop
print "Listening for callbacks from ubigraph_server on port " + str(myPort)
server.serve_forever()
