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

#include "HpiSubProviderDomain.h"


/************************************************
 * class cHpiSubProviderDomain
 ***********************************************/
cHpiSubProviderDomain::cHpiSubProviderDomain()
    : cHpiSubProvider( eHpiEntryDomain )
{
    // empty
}

cHpiSubProviderDomain::~cHpiSubProviderDomain()
{
    // empty
}

void cHpiSubProviderDomain::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForDomain( m_ctx.domain_id, txt );
}

void cHpiSubProviderDomain::GetInfo( std::deque<HpiInfo>& info ) const
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
    Line( info, L"Capabilities", di.DomainCapabilities, UI32_SaHpiDomainCapabilities );
    Line( info, L"Is Peer", di.IsPeer, UI8_SaHpiBool );
    Line( info, L"Tag", di.DomainTag );
    Line( info, L"GUID", di.Guid );

    SaHpiTimeoutT ait;
    rv = saHpiAutoInsertTimeoutGet( m_ctx.session_id, &ait );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiAutoInsertTimeoutGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Auto-Insertion Timeout, ns", ait, I64_SaHpiTimeout );
}

void cHpiSubProviderDomain::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderDomain::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderDomain::GetEntries( std::deque<HpiEntry>& entries ) const
{
    std::wstring name;

    entries.clear();

    MakeNameForDRT( name );
    entries.push_back( HpiEntry( eHpiEntryDRT, 0, name ) );
    MakeNameForRPT( name );
    entries.push_back( HpiEntry( eHpiEntryRPT, 0, name ) );
    MakeNameForDET( name );
    entries.push_back( HpiEntry( eHpiEntryDET, 0, name ) );
    MakeNameForLog( SAHPI_UNSPECIFIED_RESOURCE_ID, name );
    entries.push_back( HpiEntry( eHpiEntryLog, 0, name ) );
    MakeNameForDAT( name );
    entries.push_back( HpiEntry( eHpiEntryDAT, 0, name ) );
}

void cHpiSubProviderDomain::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    switch ( short_entry.type ) {
        case eHpiEntryDRT:
        case eHpiEntryRPT:
        case eHpiEntryDET:
        case eHpiEntryLog:
        case eHpiEntryDAT:
            ctx             = m_ctx;
            ctx.type        = short_entry.type;
            ctx.resource_id = SAHPI_UNSPECIFIED_RESOURCE_ID;
            break;
        default:
            ctx.type = eHpiEntryUnknown;
    }
}

