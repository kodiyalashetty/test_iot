
## Author Vadim Revyakin <vadim.a.revyakin@intel.com>

## Process this file with automake to produce Makefile.in

pyexec_LTLIBRARIES              = lib_ohpi.la
pyexec_DATA			= ohpi.py

EXTRA_DIST = $(pyexec_DATA)

lib_ohpi_la_SOURCES = \
	my_ohpi_wrap.c \
	lookup_funcs lookup_structs

lib_ohpi_la_CFLAGS = \
	$(HPI_CFLAGS) \
	$(PYTHON_INCLUDES)

lib_ohpi_la_LIBADD = $(HPI_LIBS)
lib_ohpi_la_LDFLAGS =

