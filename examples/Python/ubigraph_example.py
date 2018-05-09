import ubigraph

U = ubigraph.Ubigraph()
U.clear()

x = U.newVertex(shape="sphere", color="#ffff00")

smallRed = U.newVertexStyle(shape="sphere", color="#ff0000", size="0.2")

previous_r = None
for i in range(0,10):
  r = U.newVertex(style=smallRed, label=str(i))
  U.newEdge(x,r,arrow=True)
  if previous_r != None:
    U.newEdge(r,previous_r,spline=True,stroke="dashed")
  previous_r = r

    

