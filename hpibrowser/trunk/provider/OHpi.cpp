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

#include <stddef.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <string>

#include <SaHpi.h>

#include <HpiEntry.h>
#include <OHpi.h>
#include <OHpiUtils.h>

#include <stdio.h>


/************************************************
 * class cOHpi
 ***********************************************/
cOHpi::cOHpi()
    : m_selected( false ), m_selected_did( SAHPI_UNSPECIFIED_DOMAIN_ID )
{
    // empty
    // TODO saHpiInitialize?
}

cOHpi::~cOHpi()
{
    // empty
    // TODO saHpiFinalize?
}

void cOHpi::GetInfoHeader( std::wstring& txt ) const
{
    txt = L"Defined OpenHPI Domains";
}

void cOHpi::GetInfo( std::deque<HpiInfo>& ) const
{
    // empty
}

void cOHpi::GetActions( std::deque<HpiAction>& ) const
{
    // empty
}

void cOHpi::ExecuteAction( const HpiActionShort& )
{
    // empty
}

void cOHpi::GetEntries( std::deque<HpiEntry>& entries )
{
    entries.clear();

    SaErrorT rv;
    SaHpiEntryIdT id, next_id;
    oHpiDomainEntryT ode;

    bool first = true;
    id = SAHPI_FIRST_ENTRY;
    while ( id != SAHPI_LAST_ENTRY ) {
        rv = oHpiDomainEntryGet( id, &next_id, &ode );
        if ( first && ( rv == SA_ERR_HPI_NOT_PRESENT ) ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForOpenHpiDomain( ode, name );
        entries.push_back( HpiEntry( eHpiEntryDomain, ode.id, name ) );

        first = false;
        id = next_id;
    }

}

void cOHpi::Enter( const HpiEntryShort& short_entry )
{
    m_selected_did = short_entry.id;
    m_selected     = true;
    UpdateView();
}

void cOHpi::EnterNew( const std::string& host_port )
{
    if ( host_port.empty() ) {
        return;
    }

    // Parse host, host:port, [host]:port
    std::string host;
    unsigned long port = OPENHPI_DEFAULT_DAEMON_PORT;

    size_t off1, off2;
    if ( host_port[0] == '[' ) {
        off1 = 1;
        off2 = host_port.find_first_of( ']' );
        if ( off2 == std::string::npos ) {
            // Invalid host
            return;
        }
    } else {
        off1 = 0;
        off2 = host_port.find_first_of( ':' );
        if ( off2 == std::string::npos ) {
            off2 = host_port.size();
        }
    }
    host.assign( host_port.begin() + off1, host_port.begin() + off2 );
    if ( host.size() > SAHPI_MAX_TEXT_BUFFER_LENGTH ) {
        // Host is too long
        return;
    }

    off1 = host_port.find_first_of( ':', off2 );
    if ( ( off1 != std::string::npos ) && ( off1 < ( host_port.size() - 1 ) ) ) {
        std::string port_str( host_port.begin() + off1 + 1, host_port.end() );
        char *end = 0;
        port = strtoul( port_str.c_str(), &end, 10 );
        if ( ( port == 0 ) || ( ( end != 0 ) && ( *end != '\0' ) ) ) {
            // Invalid port
            return;
        }
    }

    // Prepare arguments for oHpiDomainAdd
    SaErrorT rv;
    SaHpiTextBufferT tb;
    SaHpiEntityPathT root;
    SaHpiDomainIdT did;

    tb.DataType = SAHPI_TL_TYPE_TEXT;
    tb.Language = SAHPI_LANG_ENGLISH;
    tb.DataLength = host.size();
    memcpy( &tb.Data[0], host.data(), host.size() );

    root.Entry[0].EntityType = SAHPI_ENT_ROOT;
    root.Entry[0].EntityLocation = 0;

    // Create new domain
    rv = oHpiDomainAdd( &tb, port, &root, &did );

    if ( rv == SA_OK ) {
        m_selected_did = did;
        m_selected     = true;
        UpdateView();
    }
}
