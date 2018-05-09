%module ubigraph

%inline %{
extern int    ubigraph_new_vertex();
extern int    ubigraph_new_edge(int x, int y);
extern int    ubigraph_remove_vertex(int x);
extern int    ubigraph_remove_edge(int e);
extern int    ubigraph_new_vertex_w_id(int x);
extern int    ubigraph_new_edge_w_id(int e, int x, int y);
extern void   ubigraph_clear();
extern int    ubigraph_set_vertex_attribute(int x,
              const char* attribute, const char* value);
extern int    ubigraph_change_vertex_style(int x, int s);
extern int    ubigraph_new_vertex_style(int parent_style);
extern int    ubigraph_new_vertex_style_w_id(int s,
              int parent_style);
extern int    ubigraph_set_vertex_style_attribute(int s,
              const char* attribute, const char* value);
extern int    ubigraph_set_edge_attribute(int x,
              const char* attribute, const char* value);
extern int    ubigraph_change_edge_style(int x, int s);
extern int    ubigraph_new_edge_style(int parent_style);
extern int    ubigraph_new_edge_style_w_id(int s,
              int parent_style);
extern int    ubigraph_set_edge_style_attribute(int s,
              const char* attribute, const char* value);

%}


