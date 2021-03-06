/*
 * Copyright (c) 2004 by FORCE Computers.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with the OpenHPI distribution for
 * full licensing terms.
 *
 * Authors:
 *     Thomas Kanngieser <thomas.kanngieser@fci.com>
 */

#include <glib.h>
#include "marshal.h"


int
main( int argc, char *argv[] )
{
  tFloat64      value = -47.345566;
  tFloat64      result;
  unsigned char buffer[256];

  unsigned int s1 = Marshal( &Marshal_Float64Type, &value, buffer );

  if ( s1 != sizeof( tFloat64 ) )
       return 1;

  unsigned int s2 = Demarshal( G_BYTE_ORDER, &Marshal_Float64Type, &result, buffer );

  if ( s2 != sizeof( tFloat64 ) )
       return 1;

  if ( value != result )
       return 1;

  return 0;
}
