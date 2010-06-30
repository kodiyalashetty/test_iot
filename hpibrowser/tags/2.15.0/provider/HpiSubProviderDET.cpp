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

#include "HpiSubProviderDET.h"


/************************************************
 * class cHpiSubProviderDET
 ***********************************************/
cHpiSubProviderDET::cHpiSubProviderDET()
    : cHpiSubProvider( eHpiEntryDET )
{
    // empty
}

cHpiSubProviderDET::~cHpiSubProviderDET()
{
    // empty
}

void cHpiSubProviderDET::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForDET( txt );
}

void cHpiSubProviderDET::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    Line( info, L"Domain Id", m_ctx.domain_id, UI32_SaHpiDomainId );
}

void cHpiSubProviderDET::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderDET::ExecuteAction( const HpiActionShort& )
{
}

void cHpiSubProviderDET::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;
    SaHpiEntityPathT parent, child;
    // TODO update_cnt
    SaHpiUint32T update_cnt;

    parent.Entry[0].EntityType = SAHPI_ENT_ROOT;
    parent.Entry[0].EntityLocation = 0;

    SaHpiUint32T i = SAHPI_FIRST_ENTRY;
    while( i != SAHPI_LAST_ENTRY ) {
        SaHpiUint32T entry_id = i;

        rv = saHpiGetChildEntityPath( m_ctx.session_id, parent, &i, &child, &update_cnt );
        if( rv != SA_OK ) {
            break;
        }

        std::wstring name;
        MakeNameForEntity( child, name );
        entries.push_back( HpiEntry( eHpiEntryEntity, entry_id, name ) );
    }
}

void cHpiSubProviderDET::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if( short_entry.type != eHpiEntryEntity ) {
        return;
    }

    SaErrorT rv;
    SaHpiUint32T i = short_entry.id;
    SaHpiEntityPathT parent, child;
    // TODO update_cnt
    SaHpiUint32T update_cnt;

    parent.Entry[0].EntityType = SAHPI_ENT_ROOT;
    parent.Entry[0].EntityLocation = 0;

    rv = saHpiGetChildEntityPath( m_ctx.session_id, parent, &i, &child, &update_cnt );
    if( rv != SA_OK ) {
        return;
    }

    ctx             = m_ctx;
    ctx.type        = eHpiEntryEntity;
    ctx.entity_path = child;
}

