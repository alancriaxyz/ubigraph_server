/*
 * Copyright (C) 2007 Todd Veldhuizen
 * All rights reserved
 *    
 * Written by Todd Veldhuizen.
 *      
 * Redistribution prohibited.
 *  
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
 * OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
 * OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
 * BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 * OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */


// NOT_RELEASED

extern "C" {
#include <UbigraphAPI.h>
}

#include <ubiety/benchmark/Timer.h>
#include <iostream>

using namespace std;
using namespace ubiety;

const int N = 10;

inline int idx(int i, int j, int k)
{
  return i*N*N + j*N + k;
}

void make_cube();

int main()
{
  make_cube();
}

void make_cube()
{
  Timer t;

  t.start();

  ubigraph_clear();

/*
  for (int i=0; i < N; ++i)
  {
    for (int j=0; j < N; ++j)
    {
      for (int k=0; k < N; ++k)
      {
        ubigraph_new_vertex_w_id(idx(i,j,k));
      }
    }
  }
*/

  for (int i=0; i < N; ++i)
  {
    for (int j=0; j < N; ++j)
    {
      for (int k=0; k < N; ++k)
      {
        ubigraph_new_vertex_w_id(idx(i,j,k));
        int v = idx(i,j,k);
        if (i != 0)
          ubigraph_new_edge(idx(i-1,j,k), v);
        if (j != 0)
          ubigraph_new_edge(idx(i,j-1,k), v);
        if (k != 0)
          ubigraph_new_edge(idx(i,j,k-1), v);
      }
    }
  }

  t.stop();
  cout << t.elapsedWallSeconds() << " s" << endl;
}

