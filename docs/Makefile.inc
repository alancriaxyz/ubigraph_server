.SUFFIXES:	.m4 .html

.m4.html:	header.m4 footer.m4
	rm -f $*.html
	m4 $*.m4 >$*.html
	chmod a-w $*.html
	chmod go+r $*.html

