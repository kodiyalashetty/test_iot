#!/bin/sh
# This will scan the SaHpi.h file or equivalent (required argument)
# looking for SaHpi types and generate a swig sizeof macro for it.
pass1=`egrep "SaHpi.*T;" $1`
pass2=`egrep "SaHpi.*T __attribute__\(\(__aligned__\(8\)\)\);" $1`

result1=`echo "$pass1" | sed -e 's/^.*\(Sa[A-Za-z0-9]\+T\);.*/%sizeof(\1)/g'`
result2=`echo "$pass2" | sed -e 's/^.*\(Sa[A-Za-z0-9]\+T\).*;.*/%sizeof(\1)/g'`

echo "$result2"
echo "$result1"
