#
# Copyright (c) 2003, Intel Corporation
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or 
# without modification, are permitted provided that the following 
# conditions are met:
# 
# Redistributions of source code must retain the above copyright 
# notice, this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright 
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the distribution.
# 
# Neither the name of Intel Corporation nor the names 
# of its contributors may be used to endorse or promote products 
# derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
DIAGRAMS = $(shell echo $(srcdir)/*/*png $(srcdir)/*/*gif) 

SERVER = shell1.sourceforge.net
HLDDIR = /home/groups/o/op/openhpi/htdocs/design

MAINTAINERCLEANFILES 	= Makefile.in

MOSTLYCLEANFILES = design.pdf design.ps

#openhpi_docsdir		= $(datadir)/openhpi/docs/hld

#openhpi_docs_DATA	= openhpi-manual/book1.html 

SGML_FILES              = $(shell echo $(srcdir)/*.dtd) $(shell echo $(srcdir)/*.sgml)

EXTRA_DIST		= $(DIAGRAMS) $(SGML_FILES)

all: pdf

pdf-am:
	@echo we have to do this twice to get the latex refs right
	db2pdf design.sgml
	db2pdf design.sgml

ps-am:
	@echo we have to do this twice to get the latex refs right
	db2ps design.sgml
	db2ps design.sgml

#function_docs.sgml:
#	find $(top_srcdir) -name \*\.c | xargs gnome-doc -docbook > function_docs.sgml

design/book1.html: $(SGML_FILES)
	-db2html design.sgml
	-mkdir -p design/images
	-cp $(DIAGRAMS) design/images

publish: design/book1.html
	-./htmlfilter.pl $(shell echo $(srcdir)/design/*html)
	-chmod a+x $(shell echo $(srcdir)/design/*html)
	if test ! -e design/book1.html; then \
		ln design/index.html design/book1.html; \
	fi;
	-echo "XBitHack on" > design/.htaccess
	-rsync -e ssh -rP --delete design/ $(SERVER):$(HLDDIR)
	-ssh $(SERVER) "find $(HLDDIR) -user `whoami` -exec chmod g+w {} \;"
	-ssh $(SERVER) "find $(HLDDIR) -user `whoami` -type d -exec chmod g+s {} \;"

clean:
	rm -fR design
	rm -f *~ *.tex *.aux *.log *.out
