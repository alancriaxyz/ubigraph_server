# Omit from run_all.sh

import urllib, htmllib, formatter, xmlrpclib, random, os.path, time
from urlparse import urlparse
from urlparse import urljoin
from sets import Set

# Maximum vertices to render at once
max_vertices = 100

start_url = "http://planetmath.org/encyclopedia/GraphTheory.html"

# To avoid expanding too many urls, limit ourselves to those that
# look like "/enclopedia..."
def isUrlInteresting(url):
  return (url.startswith("http://planetmath.org/encyclopedia/") 
    and url.find('#') == -1)

def brief_url(url):
  url_without_server = url.replace('http://planetmath.org/encyclopedia/', '')
  return url_without_server.replace('.html', '')

class LinksExtractor(htmllib.HTMLParser):
  def __init__(self, formatter) :        # class constructor
    htmllib.HTMLParser.__init__(self, formatter)  # base class constructor
    self.links = []        # create an empty list for storing hyperlinks

  def start_a(self, attrs) :  # override handler of <A ...>...</A> tags
    # process the attributes
    if len(attrs) > 0 :
      for attr in attrs :
        if attr[0] == "href" :         # ignore all non HREF attributes
          self.links.append(attr[1]) # save the link info in the list

  def get_links(self) :     # return the list of extracted links
    return self.links

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

G.set_edge_style_attribute(0, "spline", "true")
G.set_edge_style_attribute(0, "arrow", "true")

# Set up some styles
unopenedVertexSize = 0.5
openedVertexSize = 1.5

unopenedVertexStyle = G.new_vertex_style(0)
G.set_vertex_style_attribute(unopenedVertexStyle, "shape", "dodecahedron")
G.set_vertex_style_attribute(unopenedVertexStyle, "size", 
  str(unopenedVertexSize))
G.set_vertex_style_attribute(unopenedVertexStyle, "fontcolor", "#a0a0a0")

openedVertexStyle = G.new_vertex_style(0)
G.set_vertex_style_attribute(openedVertexStyle, "shape", "sphere")
G.set_vertex_style_attribute(openedVertexStyle, "size", str(openedVertexSize))
G.set_vertex_style_attribute(openedVertexStyle, "fontcolor", "#ffffff")
G.set_vertex_style_attribute(openedVertexStyle, "fontsize", "18")
G.set_vertex_style_attribute(openedVertexStyle, "color", "#ffff00")

expandedVertices = Set()
urlToVertex = dict()
vertexToUrl = dict()

format = formatter.NullFormatter()
htmlparser = LinksExtractor(format)

def smoothly_change_vertex_size(v, size1, size2):
  for i in range(0,6):
    G.set_vertex_attribute(v, "size", str(size1 + (i/5.0)*(size2-size1)))
    time.sleep(0.05)

def url_color(url):
  urlbits = urlparse(url)
  return str(1 + (hash(urlbits[1]) % 512))

def createurl(url):
  if (urlToVertex.has_key(url)):
    return urlToVertex[url]
  v = G.new_vertex()
  urlToVertex[url] = v
  vertexToUrl[v] = url
  G.change_vertex_style(v, unopenedVertexStyle)
  G.set_vertex_attribute(v, "label", brief_url(url))
  G.set_vertex_attribute(v, "color", url_color(url))
  return v

def expand_vertex(v):
  if (not vertexToUrl.has_key(v)):
    return -1
  if v in expandedVertices:
    return 0
  expandedVertices.add(v)
  url = vertexToUrl[v]
  print ""
  print "Expanding " + url
  print "===================================="
  G.set_vertex_attribute(v, "color", "#ffff00")
  smoothly_change_vertex_size(v, unopenedVertexSize, 3.0)
  G.set_vertex_attribute(v, "label", "Working: " + brief_url(url))
  G.set_vertex_attribute(v, "fontcolor", "#ff0000")
  G.set_vertex_attribute(v, "fontsize", "24")
  urlbits = urlparse(url)
  data = urllib.urlopen(url)
  htmlparser.feed(data.read())
  htmlparser.close()
  links = htmlparser.get_links()
  G.set_vertex_attribute(v, "fontcolor", "#ffffff")
  G.set_vertex_attribute(v, "shape", "sphere")
  
  unique_links = Set()
  for url2 in links:
    url2 = urljoin(url, url2)
    print "urljoin(" + url + ", " + url2 + ") = " + url2
    unique_links.add(url2)

  print ""
  print "Unique links:"
  for url2 in unique_links:
    print url2
    if (url2 != url) and isUrlInteresting(url2):
      v2 = createurl(url2)
      G.new_edge(v,v2)
  smoothly_change_vertex_size(v, 3.0, openedVertexSize)
  G.change_vertex_style(v, openedVertexStyle)
  G.set_vertex_attribute(v, "label", brief_url(url))
  return 0

root = createurl(start_url)

note = G.new_vertex()
G.set_vertex_attribute(note, "shape", "none")
G.set_vertex_attribute(note, "label", "Left-doubleclick to expand a node")
G.set_vertex_attribute(note, "fontsize", "18")
e = G.new_edge(note,root)
G.set_edge_attribute(e, "visible", "false")
G.set_edge_attribute(e, "oriented", "true")

expand_vertex(root)

time.sleep(1)
G.remove_vertex(note)

# Now make our callback engine.  Pick a random port (so that
# uncompleted teardowns don't prevent us from running this 
# code twice in a row).
myPort = random.randint(20739,20999)

# Set up a callback for left double-clicks on vertices.
G.set_vertex_style_attribute(0, "callback_left_doubleclick",
  "http://127.0.0.1:" + str(myPort) + "/expand_vertex")

# Now make an XMLRPC server to handle tha callbacks.
from SimpleXMLRPCServer import SimpleXMLRPCServer

# Create server
server = SimpleXMLRPCServer(("localhost", myPort))
server.register_introspection_functions()

server.register_function(expand_vertex)

# Run the server's main loop
print "Listening for callbacks from ubigraph_server on port " + str(myPort)
server.serve_forever()

