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

#include "HpiSubProviderReset.h"


/************************************************
 * class cHpiSubProviderReset
 ***********************************************/
cHpiSubProviderReset::cHpiSubProviderReset()
    : cHpiSubProvider( eHpiEntryReset )
{
    // empty
}

cHpiSubProviderReset::~cHpiSubProviderReset()
{
    // empty
}

void cHpiSubProviderReset::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForReset( txt );
}

void cHpiSubProviderReset::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );

    SaErrorT rv;
    SaHpiResetActionT reset_action;

    rv = saHpiResourceResetStateGet( m_ctx.session_id, m_ctx.resource_id, &reset_action );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiResourceResetStateGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"State", reset_action );
}

void cHpiSubProviderReset::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderReset::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderReset::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderReset::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

