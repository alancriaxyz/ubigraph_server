# Ubigraph

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

Ubigraph is a different way to create interactive user interfaces with the purpose of visualizing huge amounts of data. Its visualizations are simply stunning. This version is shipped in binary form as a standalone server that responds to requests using XML-RPC. This makes it easy to use from C, C++, Java, Ruby, Python, Perl, and other languages for which XML-RPC implementations are available. Since XML-RPC uses TCP-IP, the server (which visualizes the graph) can be run on a different machine/operating system than the client (which is manipulating the graph). It is also possible to have multiple clients updating the graph simultaneously. (Note that for clients to be on different machines from the server, firewalls must be configured to allow traffic on port 20738.)


