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

#include "HpiSubProviderRPT.h"


/************************************************
 * class cHpiSubProviderRPT
 ***********************************************/
cHpiSubProviderRPT::cHpiSubProviderRPT()
    : cHpiSubProvider( eHpiEntryRPT )
{
    // empty
}

cHpiSubProviderRPT::~cHpiSubProviderRPT()
{
    // empty
}

void cHpiSubProviderRPT::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForRPT( txt );
}

void cHpiSubProviderRPT::GetInfo( std::deque<HpiInfo>& info ) const
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
    Line( info, L"Update Count", di.RptUpdateCount );
    Line( info, L"Update Timestamp", di.RptUpdateTimestamp, I64_SaHpiTime );
}

void cHpiSubProviderRPT::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderRPT::ExecuteAction( const HpiActionShort& )
{
}

void cHpiSubProviderRPT::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;
    SaHpiEntryIdT id, next_id;
    SaHpiRptEntryT rpte;

    bool first = true;
    id = SAHPI_FIRST_ENTRY;
    while ( id != SAHPI_LAST_ENTRY ) {
        rv = saHpiRptEntryGet( m_ctx.session_id, id, &next_id, &rpte );
        if ( first && ( rv == SA_ERR_HPI_NOT_PRESENT ) ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForResource( rpte, name );
        entries.push_back( HpiEntry( eHpiEntryResource, rpte.ResourceId, name ) );

        first = false;
        id = next_id;
    }
}

void cHpiSubProviderRPT::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if ( short_entry.type != eHpiEntryResource ) {
        return;
    }

    ctx             = m_ctx;
    ctx.type        = eHpiEntryResource;
    ctx.resource_id = short_entry.id;
}

