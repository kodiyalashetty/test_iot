# (C) Copyright IBM Corp 2005
# All rights reserved.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
# file and program are licensed under a BSD style license.  See
# the Copying file included with the OpenHPI distribution for
# full licensing terms.

MOSTLYCLEANFILES 	= @TEST_CLEAN@ uid_map
EXTRA_DIST              = openhpi.conf

INCLUDES		= @OPENHPI_INCLUDES@

AM_CFLAGS		= @NOCFLAGS@

MAINTAINERCLEANFILES 	= Makefile.in

# removed until the gcc 3.4 bug is fixed
# -ftest-coverage -fprofile-arcs
TDEPLIB			= $(top_builddir)/src/libopenhpi.la \
			  $(top_builddir)/utils/libopenhpiutils.la

TESTS_ENVIRONMENT = OPENHPI_PATH=$(top_builddir)/plugins/simulator
TESTS_ENVIRONMENT += OPENHPI_UID_MAP=$(shell pwd)/uid_map
TESTS_ENVIRONMENT += OPENHPI_CONF=./openhpi.conf

TESTS = sim_sanity_000 \
	sim_sanity_001 \
	sim_sanity_002 \
	sim_sanity_003 \
	sim_sanity_004 \
	sim_sanity_005 \
	sim_sanity_006 \
	sim_sanity_007 \
	sim_sanity_008 \
	sim_sanity_009 \
	sim_sanity_010 \
	sim_sanity_011 \
	sim_sanity_012 \
	sim_sanity_013 \
	sim_sanity_014 \
	sim_sanity_015 \
	sim_sanity_016 \
	sim_sanity_017 \
	sim_sanity_018 \
	sim_sanity_019 \
	sim_sanity_020
#	sim_sanity_100 \
#	sim_sanity_101 \
#	sim_sanity_102

check_PROGRAMS = $(TESTS)

sim_sanity_000_SOURCES = sim_sanity_000.c
sim_sanity_000_LDADD = $(TDEPLIB)
sim_sanity_001_SOURCES = sim_sanity_001.c
sim_sanity_001_LDADD = $(TDEPLIB)
sim_sanity_002_SOURCES = sim_sanity_002.c
sim_sanity_002_LDADD = $(TDEPLIB)
sim_sanity_003_SOURCES = sim_sanity_003.c
sim_sanity_003_LDADD = $(TDEPLIB)
sim_sanity_004_SOURCES = sim_sanity_004.c
sim_sanity_004_LDADD = $(TDEPLIB)
sim_sanity_005_SOURCES = sim_sanity_005.c
sim_sanity_005_LDADD = $(TDEPLIB)
sim_sanity_006_SOURCES = sim_sanity_006.c
sim_sanity_006_LDADD = $(TDEPLIB)
sim_sanity_007_SOURCES = sim_sanity_007.c
sim_sanity_007_LDADD = $(TDEPLIB)
sim_sanity_008_SOURCES = sim_sanity_008.c
sim_sanity_008_LDADD = $(TDEPLIB)
sim_sanity_009_SOURCES = sim_sanity_009.c
sim_sanity_009_LDADD = $(TDEPLIB)
sim_sanity_010_SOURCES = sim_sanity_010.c
sim_sanity_010_LDADD = $(TDEPLIB)
sim_sanity_011_SOURCES = sim_sanity_011.c
sim_sanity_011_LDADD = $(TDEPLIB)
sim_sanity_012_SOURCES = sim_sanity_012.c
sim_sanity_012_LDADD = $(TDEPLIB)
sim_sanity_013_SOURCES = sim_sanity_013.c
sim_sanity_013_LDADD = $(TDEPLIB)
sim_sanity_014_SOURCES = sim_sanity_014.c
sim_sanity_014_LDADD = $(TDEPLIB)
sim_sanity_015_SOURCES = sim_sanity_015.c
sim_sanity_015_LDADD = $(TDEPLIB)
sim_sanity_016_SOURCES = sim_sanity_016.c
sim_sanity_016_LDADD = $(TDEPLIB)
sim_sanity_017_SOURCES = sim_sanity_017.c
sim_sanity_017_LDADD = $(TDEPLIB)
sim_sanity_018_SOURCES = sim_sanity_018.c
sim_sanity_018_LDADD = $(TDEPLIB)
sim_sanity_019_SOURCES = sim_sanity_019.c
sim_sanity_019_LDADD = $(TDEPLIB)
sim_sanity_020_SOURCES = sim_sanity_020.c
sim_sanity_020_LDADD = $(TDEPLIB)
sim_sanity_100_SOURCES = sim_sanity_100.c
sim_sanity_100_LDADD = $(TDEPLIB)
sim_sanity_101_SOURCES = sim_sanity_101.c
sim_sanity_101_LDADD = $(TDEPLIB)
sim_sanity_102_SOURCES = sim_sanity_102.c
sim_sanity_102_LDADD = $(TDEPLIB)
