import org.ubiety.ubigraph.UbigraphClient;

public class Example {

public static void main(String[] args) 
{
  UbigraphClient graph = new UbigraphClient();

  int N = 10;
  int[] vertices = new int[N];

  for (int i=0; i < N; ++i)
    vertices[i] = graph.newVertex();

  for (int i=0; i < N; ++i)
    graph.newEdge(vertices[i], vertices[(i+1)%N]);
}

}

