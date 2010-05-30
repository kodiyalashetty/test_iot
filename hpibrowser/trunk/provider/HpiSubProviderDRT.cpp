/*
 *  Copyright (c) 2010 Pigeon Point Systems.
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
 *     Sergey Ivushkin (Pigeon Point Systems)
 */


#include <HpiUtils.h>

#include "HpiSubProviderDRT.h"


/************************************************
 * class cHpiSubProviderDRT
 ***********************************************/
cHpiSubProviderDRT::cHpiSubProviderDRT()
    : cHpiSubProvider( eHpiEntryDRT )
{
    // empty
}

cHpiSubProviderDRT::~cHpiSubProviderDRT()
{
    // empty
}

void cHpiSubProviderDRT::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForDRT( txt );
}

void cHpiSubProviderDRT::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiDomainInfoT di;

    rv = saHpiDomainInfoGet( m_ctx.session_id, &di );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiDomainInfoGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Domain Id", di.DomainId, UI32_SaHpiDomainId );
    Line( info, L"Update Count", di.DrtUpdateCount );
    Line( info, L"Update Timestamp", di.DrtUpdateTimestamp, I64_SaHpiTime );
}

void cHpiSubProviderDRT::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderDRT::ExecuteAction( const HpiActionShort& )
{
}

void cHpiSubProviderDRT::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;
    SaHpiEntryIdT id, next_id;
    SaHpiDrtEntryT drte;

    bool first = true;
    id = SAHPI_FIRST_ENTRY;
    while ( id != SAHPI_LAST_ENTRY ) {
        rv = saHpiDrtEntryGet( m_ctx.session_id, id, &next_id, &drte );
        if ( first && ( rv == SA_ERR_HPI_NOT_PRESENT ) ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForDomain( drte.DomainId, name );
        entries.push_back( HpiEntry( eHpiEntryResource, drte.EntryId, name ) );

        first = false;
        id = next_id;
    }
}

void cHpiSubProviderDRT::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if ( short_entry.type != eHpiEntryResource ) {
        return;
    }

    SaErrorT rv;
    SaHpiEntryIdT next_id;
    SaHpiDrtEntryT drte;

    rv = saHpiDrtEntryGet( m_ctx.session_id, short_entry.id, &next_id, &drte );
    if ( rv != SA_OK ) {
        return;
    }

    ctx             = m_ctx;
    ctx.type        = eHpiEntryDomain;
    ctx.resource_id = drte.DomainId;
}

