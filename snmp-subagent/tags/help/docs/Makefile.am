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
DIAGRAMS = $(shell ls  images/*jpg) 

SFUSER = $(shell if test $(SFUID) != "" > /dev/null 2>&1; then echo $(SFUID); else echo $(USER);fi;)
SERVER = shell1.sourceforge.net
HLDDIR = /home/groups/o/op/openhpi/htdocs/subagent-manual

MAINTAINERCLEANFILES 	= Makefile.in  

subagent_docsdir		= $(datadir)/subagent/docs


SGML_FILES              = $(shell ls *.dtd) $(shell ls *.sgml)

EXTRA_DIST		= $(DIAGRAMS) $(SGML_FILES)

all:

pdf-am:
	@echo we have to do this twice to get the latex refs right
	db2pdf subagent-manual.sgml
	db2pdf subagent-manual.sgml

ps-am:
	@echo we have to do this twice to get the latex refs right
	db2ps subagent-manual.sgml
	db2ps subagent-manual.sgml

#function_docs.sgml:
#	find $(top_srcdir) -name \*\.c | xargs gnome-doc -docbook > function_docs.sgml

subagent-manual/book1.html: $(SGML_FILES)
	-db2html -o subagent-manual subagent-manual.sgml
	-mkdir -p subagent-manual/images
	-cp $(DIAGRAMS) subagent-manual/images
	-./htmlfilter.pl subagent-manual/*html 

publish: subagent-manual/book1.html
	-chmod a+x subagent-manual/*html
	if [ ! -e subagent-manual/book1.html ]; then \
		ln subagent-manual/index.html subagent-manual/book1.html; \
	fi;
	-echo "XBitHack on" > subagent-manual/.htaccess
	-rsync -e ssh -rP --delete subagent-manual/ $(SFUSER)@$(SERVER):$(HLDDIR)
	-ssh $(SFUSER)@$(SERVER) "find $(HLDDIR) -user `whoami` -exec chmod g+w {} \;"
	-ssh $(SFUSER)@$(SERVER) "find $(HLDDIR) -user `whoami` -type d -exec chmod g+s {} \;"

clean:
	rm -fR subagent-manual
	rm -f *~ *.tex *.aux *.log *.out
