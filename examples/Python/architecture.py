import ubigraph, sys

#Omit
U = ubigraph.Ubigraph()
U.clear()

U.defaultVertexStyle.set(fontsize=14)
engine = U.newVertex(color="#ffff00",shape="dodecahedron",label="LayoutEngine")
server = U.newVertex(color="#8080ff",shape="cube",label="XMLRPC Server")
engine_server_edge = U.newEdge(server,engine,width=3,arrow=True,oriented=True)

def client():
  clientXVertex = U.newVertex(color="#8080ff",shape="cube",label="XMLRPC Client")
  clientVertex = U.newVertex(color="#ff0080",shape="cube",label="Client App")
  U.newEdge(clientVertex,clientXVertex,arrow=True,oriented=True)
  U.newEdge(clientXVertex,server,arrow=True,oriented=True)

for i in range(0,3):
  client()
  sys.stdin.readline()

