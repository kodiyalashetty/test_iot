#!/usr/bin/perl
#
# (C) Copyright IBM Corp. 2004
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
# file and program are licensed under a BSD style license.  See
# the Copying file included with the OpenHPI distribution for
# full licensing terms.
#
# Convert a text file into a C program string declaration
#
# Author(s):
#      W. David Ashley <dashley@us.ibm.com>
#
eval "exec /usr/bin/perl -S $0 $*"
	if $Shell_cannot_understand; #!

$0 =~ /[^\/]+$/ ;	# get the name of this program
$program = $&;
$sflag = 0;
$strname = "eventxml";
while($_ = $ARGV[0], /^-/){ # get options
	shift;
	if(/^-s$/){ $sflag = 1; $strname = $ARGV[0]; shift; }
	elsif(/^-s(.*)/){ $sflag = 1; $strname = $1; }
	else{
		print stderr "$program: convert text to C program string...\n";
                print stderr "  Usage: $program -s strname ] { textfile }\n";
		exit 0;
	}
}
print "\n";
print "char *$strname" . " = {\n";
while(<>){
	chop;
	s/\\/\\\\/g;
	s/\t/\\t/g;
	s/\"/\\"/g;
	print "\t\"$_\\n\"\n";
}
print "\t\"\\0\"\n";
print "};\n";
print "\n";
