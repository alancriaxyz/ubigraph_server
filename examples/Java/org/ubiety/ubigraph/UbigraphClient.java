package org.ubiety.ubigraph;

import java.net.*;
import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;
import org.apache.xmlrpc.XmlRpcException;

/**
 * Java language interface to a Ubigraph server via XMLRPC.
 * @author Todd Veldhuizen
 */

public class UbigraphClient {

XmlRpcClient client;

/**
 * Connects to the ubigraph server.  By default, the url
 * http://127.0.0.1:20738/RPC2 (localhost, port 20738) is
 * used.
 */
public UbigraphClient()
{
  XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();
  try {
    config.setServerURL(new URL("http://127.0.0.1:20738/RPC2"));
    client = new XmlRpcClient();
    client.setConfig(config);
  } catch(Exception e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Connects to the ubigraph server using an alternate URL.
 */
public UbigraphClient(String url)
{
  XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();
  try {
    config.setServerURL(new URL(url));
    client = new XmlRpcClient();
    client.setConfig(config);
  } catch(Exception e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Create a new vertex.
 * @return The vertexId of the new vertex.
 */
public int newVertex() 
{
  try {
    Object[] params = new Object[]{};
    Integer result = (Integer)client.execute("ubigraph.new_vertex", 
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Create a new vertex with a specified vertexId.
 * @return 0 if success, -1 if failure (a vertex with that id exists already).
 */
public int newVertex(int vertexId) 
{
  try {
    Object[] params = new Object[]{new Integer(vertexId)};
    Integer result = (Integer)client.execute("ubigraph.new_vertex_w_id", 
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Deletes the vertex.
 * @return 0 if success, -1 if failure.
 */
public int removeVertex(int vertexId)
{
  try {
    Object[] params = new Object[]{new Integer(vertexId)};
    Integer result = (Integer)client.execute("ubigraph.remove_vertex", 
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Create a new edge between two vertices.
 * @param i Source vertex of edge
 * @param j Destination vertex of edge
 * @return The edgeId for the new edge.
 */
public int newEdge(int i, int j) 
{
  try {
    Object[] params = new Object[]{new Integer(i), new Integer(j)};
    Integer result = (Integer) client.execute("ubigraph.new_edge", 
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Create a new edge with a specified edgeId.
 * @return 0 if success, -1 if failure (edge already exists).
 */
public int newEdge(int edgeId, int i, int j) 
{
  try {
    Object[] params = new Object[]{new Integer(edgeId), new Integer(i),
      new Integer(j)};
    Integer result = (Integer) client.execute("ubigraph.new_edge_w_id", 
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Removes an edge.
 * @return 0 if success, -1 if failure (edge does not exist).
 */
public int removeEdge(int edgeId)
{
  try {
    Object[] params = new Object[]{new Integer(edgeId)};
    Integer result = (Integer)client.execute("ubigraph.remove_edge",
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Set an attribute of a vertex.  See the Ubigraph XMLRPC manual
 * for details of what attributes can be set.  
 * Some basic attributes are:
 * <ul>
 *  <li>shape: sphere, cone, torus, tetrahedron, cube, octahedron, 
 *             dodecahedron, icosahedron</li>
 *  <li>label: a string to be displayed near the vertex</li>
 *  <li>color: e.g. "#ff0000"</li>
 * </ul>
 * @param attribute The name of the attribute to be changed, e.g., "color",
 *                  "shape", "label", etc.
 * @param value The new value for the attribute.  
 */
public int setVertexAttribute(int vertexId, String attribute, String value)
{
  try {
    Object[] params = new Object[]{new Integer(vertexId), attribute,
      value };
    Integer result = (Integer) client.execute("ubigraph.set_vertex_attribute",
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Create a new vertex style.  
 * @param parent_styleId  The style on which to base the new style.  Use
 *                        0 for the default vertex style.
 * @return styleId
 */
public int newVertexStyle(int parent_styleId)
{
  try {
    Object[] params = new Object[]{new Integer(parent_styleId)};
    Integer result = (Integer) client.execute("ubigraph.new_vertex_style",
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/** 
 * Create a new vertex style.  
 * @param styleId         The desired styleId to create.
 * @param parent_styleId  The style on which to base the new style.  Use
 *                        0 for the default vertex style.
 * @return 0 on success, -1 if the desired styleId already exists
 */
public int newVertexStyle(int styleId, int parent_styleId)
{
  try {
    Object[] params = new Object[]{new Integer(styleId),
      new Integer(parent_styleId)};
    Integer result = (Integer) client.execute("ubigraph.new_vertex_style_w_id",
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  } 
}

/**
 * Set an attribute of a style.  See also setVertexAttribute().
 * @param styleId  The style to modify.  Use 0 for the default vertex style.
 * @return 0 on success, -1 on failure
 */
public int setVertexStyleAttribute(int styleId, String attribute, String value)
{
  try {
    Object[] params = new Object[]{new Integer(styleId), attribute, value};
    Integer result = (Integer) client.execute(
      "ubigraph.set_vertex_style_attribute", params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Change a vertex to a specified style
 * @return 0 on success, -1 on failure
 */
public int changeVertexStyle(int vertexId, int styleId) 
{
  try {
    Object[] params = new Object[]{new Integer(vertexId), new Integer(styleId) };
    Integer result = (Integer) client.execute("ubigraph.change_vertex_style",
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/** 
 * Create a new edge style.  
 * @param parent_styleId  The style on which to base the new style.  Use
 *                        0 for the default edge style.
 * @return styleId
 */
public int newEdgeStyle(int parent_styleId)
{
  try {
    Object[] params = new Object[]{new Integer(parent_styleId)};
    Integer result = (Integer) client.execute("ubigraph.new_edge_style",
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }   
}   

/** 
 * Create a new edge style.  
 * @param styleId         The desired styleId to create.
 * @param parent_styleId  The style on which to base the new style.  Use
 *                        0 for the default edge style.
 * @return 0 if success, -1 if styleId is already in use.
 */
public int newEdgeStyle(int styleId, int parent_styleId)
{
  try {
    Object[] params = new Object[]{new Integer(styleId), 
      new Integer(parent_styleId)};
    Integer result = (Integer) client.execute("ubigraph.new_edge_style_w_id",
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/** 
 * Set an attribute of a style.  See also setVertexAttribute().
 * @param styleId  The style to modify.  Use 0 for the default edge style.
 * @return 0 on success, -1 on failure
 */
public int setEdgeStyleAttribute(int styleId, String attribute, String value)
{
  try {
    Object[] params = new Object[]{new Integer(styleId), attribute, value};
    Integer result = (Integer) client.execute(
      "ubigraph.set_edge_style_attribute", params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Change an edge to a specified style
 * @return 0 on success, -1 on failure
 */
public int changeEdgeStyle(int edgeId, int styleId) 
{     
  try {
    Object[] params = new Object[]{new Integer(edgeId), new Integer(styleId) };   
    Integer result = (Integer) client.execute("ubigraph.change_edge_style",
      params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

/**
 * Remove all vertices and edges from the graph, and reset styles.
 */
public int clear()
{
  try {
    Object[] params = new Object[]{};
    Integer result = (Integer)client.execute("ubigraph.clear", params);
    return result.intValue();
  } catch(XmlRpcException e) {
    throw new RuntimeException(e.getMessage());
  }
}

}

