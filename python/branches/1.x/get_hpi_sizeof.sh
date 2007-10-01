#!/bin/sh
# This will scan the SaHpi.h file or equivalent (required argument)
# looking for SaHpi types and generate a swig sizeof macro for it.
egrep "SaHpi.*T;" $1 | sed -e 's/^.*\(Sa[A-Za-z0-9]\+T\);.*/%sizeof(\1)/g'
