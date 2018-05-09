import xmlrpclib
import time

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

# This example draws a tree.  There are two kinds of edges:
# tree_edge: structural edges for the tree that links parents to kids
# next_edge: edges showing inorder traversal order.
# By changing styles, we can highlight one kind of structure or another.

# All edges will be oriented
G.set_edge_style_attribute(0, "oriented", "true")

tree_edge = G.new_edge_style(0)
G.set_edge_style_attribute(tree_edge, "color", "#ffff00")

next_edge = G.new_edge_style(0)
G.set_edge_style_attribute(next_edge, "color", "#00ff00")


# Create the tree edges

# Bear with me... I wrote this before I knew Python

#    d 
#   / \
#  b   f 
# / \ / \
#a  c e g

a = G.new_vertex()
G.set_vertex_attribute(a, "label", "a")
b = G.new_vertex()
G.set_vertex_attribute(b, "label", "b")
c = G.new_vertex()
G.set_vertex_attribute(c, "label", "c")
d = G.new_vertex()
G.set_vertex_attribute(d, "label", "d")
e = G.new_vertex()
G.set_vertex_attribute(e, "label", "e")
f = G.new_vertex()
G.set_vertex_attribute(f, "label", "f")
g = G.new_vertex()
G.set_vertex_attribute(g, "label", "g")

ba = G.new_edge(b,a)
bc = G.new_edge(b,c)
db = G.new_edge(d,b)
df = G.new_edge(d,f)
fe = G.new_edge(f,e)
fg = G.new_edge(f,g)

G.change_edge_style(ba, tree_edge)
G.change_edge_style(bc, tree_edge)
G.change_edge_style(db, tree_edge)
G.change_edge_style(df, tree_edge)
G.change_edge_style(fe, tree_edge)
G.change_edge_style(fg, tree_edge)

# Next pointers

ab2 = G.new_edge(a,b)
bc2 = G.new_edge(b,c)
cd2 = G.new_edge(c,d)
de2 = G.new_edge(d,e)
ef2 = G.new_edge(e,f)
fg2 = G.new_edge(f,g)

G.change_edge_style(ab2, next_edge)
G.change_edge_style(bc2, next_edge)
G.change_edge_style(cd2, next_edge)
G.change_edge_style(de2, next_edge)
G.change_edge_style(ef2, next_edge)
G.change_edge_style(fg2, next_edge)

# Now we're going to illustratet how you can change the visual
# structure of the graph to reveal or hide aspects, just by 
# changing style attributes.

def transitionEdgeStrengths(styleid_strong, styleid_weak):
  for i in range(0,10):
    a = i / 9.0
    G.set_edge_style_attribute(styleid_strong, "strength", str(a))
    G.set_edge_style_attribute(styleid_weak, "strength", str(1.0-a))
    time.sleep(0.1)

def highlightEdgeStyle(styleid):
  G.set_edge_style_attribute(styleid, "arrow", "true");
  G.set_edge_style_attribute(styleid, "stroke", "solid");
  G.set_edge_style_attribute(styleid, "width", "2.0")
  G.set_edge_style_attribute(styleid, "spline", "false")

def deemphasizeEdgeStyle(styleid):
  G.set_edge_style_attribute(styleid, "arrow", "false");
  G.set_edge_style_attribute(styleid, "stroke", "dotted");
  G.set_edge_style_attribute(styleid, "width", "1.0")
  G.set_edge_style_attribute(styleid, "spline", "true")

tetheredLabel = G.new_vertex()
tether = G.new_edge(tetheredLabel, a)
G.set_edge_attribute(tether, "visible", "false")
G.set_vertex_attribute(tetheredLabel, "shape", "none")

for k in range(0,2):
  G.set_vertex_attribute(tetheredLabel, "label", "")
  transitionEdgeStrengths(tree_edge,next_edge)
  highlightEdgeStyle(tree_edge)
  deemphasizeEdgeStyle(next_edge)
  G.set_vertex_attribute(tetheredLabel, "label", "Showing tree structure")
  time.sleep(3)
  G.set_vertex_attribute(tetheredLabel, "label", "")
  transitionEdgeStrengths(next_edge,tree_edge)
  highlightEdgeStyle(next_edge)
  deemphasizeEdgeStyle(tree_edge)
  G.set_vertex_attribute(tetheredLabel, "label", "Showing 'next' pointers")
  time.sleep(3)

