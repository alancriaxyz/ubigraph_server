#include <stdio.h>
#include <map>
#include <string>
#include <math.h>
#include <iostream>

extern "C" {
#include <UbigraphAPI.h>
}

using namespace std;

typedef map<string,vertex_id_t> map_t;
map_t dirs;

typedef map<vertex_id_t,int> sizemap_t;
sizemap_t sizes;

vertex_id_t getvertex(string dirname)
{
  map_t::iterator iter = dirs.find(dirname);
  if (iter == dirs.end())
  {
    vertex_id_t x = ubigraph_new_vertex();
    dirs.insert(pair<string,vertex_id_t>(dirname,x));
    return x;
  }
  else
    return iter->second;
}

char* split(char* dirname);
void label(char* dirname, int size, bool replace);

int main()
{
  char tbuf[1024];

  ubigraph_clear();
  ubigraph_set_edge_style_attribute(0, "oriented", "true");
  ubigraph_set_vertex_style_attribute(0, "shape", "sphere");

  FILE* src = popen("du -k /Users/tveldhui", "r");
  
  int vid = 0;

  while (fgets(tbuf, 1024, src))
  {
//    printf("%s", tbuf);

    int size;
    sscanf(tbuf, "%d", &size);
    if (size < 128L*1024)
      continue;

    char* dirname = 0;
    for (int i=0; i < 1024; ++i)
    {
      if (tbuf[i] == 0x09)
      {
        dirname = tbuf + i + 1;
        break; 
      }
    }
    tbuf[strlen(tbuf)-1] = 0;
    label(dirname, size, true);
  }

  pclose(src);
}

char* split(char* dirname)
{
    for (int k=strlen(dirname)-1; k > 0; --k)
    {
      if (dirname[k] == '/')
      {
        dirname[k] = 0;
        return dirname + k + 1;
      }
    }
  return 0;
}

int hash(int x, int y)
{
  return abs(93142*x + y);
}

void label(char* dirname, int size, bool replace)
{
  int prevsize = 0;

  vertex_id_t x = getvertex(dirname);

  if (sizes.find(x) != sizes.end())
  {
    prevsize = sizes[x];
    sizes.erase(x);
  }
 
  int totsize = prevsize + size;
  if (replace)
    totsize = size;

  sizes.insert(pair<vertex_id_t,int>(x, totsize));

  double dsize = (1 + 2*log10(totsize / (1024*1024.0))) / 2.0;
  
  if (dsize < 0.3)
    dsize = 0.3;
  double gb = totsize / 1024.0 / 1024.0;
  
  char tmp[40];
  sprintf(tmp, "%lf", dsize);
  ubigraph_set_vertex_attribute(x, "size", tmp);

  bool wasRoot = !strcmp(dirname, "/Users");

  char* pathlessName = split(dirname);
  if (pathlessName != 0)
  {
    if (!wasRoot)
    {
    vertex_id_t y = getvertex(dirname);
    ubigraph_new_edge_w_id(hash(y,x),y,x);

    if (replace)
      label(dirname, totsize - prevsize, false);   
    else
      label(dirname, size, false);
    }

  if (gb >= 1.0)
  {
    char xbuf[1000];
    sprintf(xbuf, "%s (%d Gb)", pathlessName, (int)gb);
    ubigraph_set_vertex_attribute(x, "label", xbuf);
    ubigraph_set_vertex_attribute(x, "fontsize", "18");
  }
  else if (gb > 0.25) {
    ubigraph_set_vertex_attribute(x, "label", pathlessName);
    ubigraph_set_vertex_attribute(x, "fontcolor", "#a0a0a0");
  }
  }
}

