/*
 *  Copyright (c) 2012 Pigeon Point Systems.
 *  All rights reserved.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 * file and program are licensed under a BSD style license.  See
 * the Copying file included with this distribution for
 * full licensing terms.
 *
 * Authors:
 *     Anton Pak (Pigeon Point Systems)
 */

#include <string>

#include <HpiUtils.h>
#include <OHpiUtils.h>


#ifdef _WIN32
#define swprintf _snwprintf
#endif


void MakeNameForOpenHpiDomain( const oHpiDomainEntryT& ode, std::wstring& txt )
{

    std::wstring id;
    MakeNameForDomain( ode.id, id );

    std::wstring host;
    ToTxt( ode.host, host );

    wchar_t buf[4096];
    swprintf( buf,
              sizeof(buf) / sizeof(wchar_t),
              L"%ls:  Host %ls  Port %u",
              id.c_str(),
              host.c_str(),
              (unsigned int)ode.port );
    txt = buf;
}

