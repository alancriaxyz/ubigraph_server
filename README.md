# Ubigraph

![Image of Ubigraph](http://holsee.github.io/images/exconfeu/erlubi_vanilla.png)

Ubigraph is a different way to create interactive user interfaces with the purpose of visualizing huge amounts of data. Its visualizations are simply stunning. This version is shipped in binary form as a standalone server that responds to requests using XML-RPC. This makes it easy to use from C, C++, Java, Ruby, Python, Perl, and other languages for which XML-RPC implementations are available. Since XML-RPC uses TCP-IP, the server (which visualizes the graph) can be run on a different machine/operating system than the client (which is manipulating the graph). It is also possible to have multiple clients updating the graph simultaneously. (Note that for clients to be on different machines from the server, firewalls must be configured to allow traffic on port 20738.)

# Why does this repository exist?

Ubigraph was developed by ubietylab, but the project has stopped receiving updates since 2008. Also it is not possible to download the latest version through the official website (http://ubietylab.net/ubigraph/content/Downloads/index.php).

I was able to find the latest version (alpha-0.2.4, June 2008) and thought that making it available here in github would be easier for other developers to use this amazing tool. Besides using I think that others can continue to contribute to the improvement and those who know how to bring new versions.

I hope ubietylab can look at this repository and keep contributing to this beautiful project.


