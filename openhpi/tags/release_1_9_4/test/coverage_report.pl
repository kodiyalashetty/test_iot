#!/usr/bin/perl

#       $Id$
 
#  (C) Copyright IBM Corp. 2004
 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
#  file and program are licensed under a BSD style license.  See
#  the Copying file included with the OpenHPI distribution for
#  full licensing terms.
 
#  Authors:
#      Sean Dague <http://dague.net/sean>

use strict;

my @dirs = qw(src utils plugins/snmp_bc plugins/snmp_bc/t);

my $outdir = "report_html";

mkdir $outdir, 0755;

foreach my $dir (@dirs) {
    opendir(DIR,"../$dir");
    while(my $file = readdir(DIR)) {
        my $safename = $dir;
        $safename =~ s{/}{_}g;
        $safename .= "_";
        if($file =~ /\.gcov$/) {
            system("./gcov2html.pl ../$dir/$file > $outdir/$safename$file.html");
        } elsif ($file =~ /\.summary$/) {
            system("./gsum2html.pl ../$dir/$file > $outdir/$safename$file.html");
        }
    }
    closedir(DIR);
}

system("./generate_index.pl $outdir > $outdir/index.html");

