BASEPATH=../../../..
include $(BASEPATH)/Makefile.inc
CC = gcc
CCFLAGS = -g 
LIBS = -lpthread $(OS_LIBS) $(SUPPORT_LIBS) $(SUPPORT_LIBS) $(SUPPORT_LIBS)
# -L. -L/usr/lib -lm -lcurl -lubigraphclient -lxmlrpc_client -lxmlrpc -lxmlrpc_util -lxmlrpc_xmlparse -lxmlrpc_xmltok

PYTHON_INCLUDE = -I/System/Library/Frameworks/Python.framework/Versions/2.3/include/python2.3 -I/System/Library/Frameworks/Python.framework/Versions/2.3/lib/python2.3/config

TARGETS = _ubigraph.so

.SUFFIXES:	.c

all:	$(TARGETS)

ubigraph_wrap.c:	ubigraph.i
	swig -python ubigraph.i

_ubigraph.so:	../client.o ubigraph_wrap.o
	$(CC) -bundle -undefined suppress -flat_namespace ../client.o ubigraph_wrap.o -o _ubigraph.so $(LIBS)

libubigraphclient:	client.o
	ar -r libubigraphclient.a client.o

clean:
	rm -f $(TARGETS)

