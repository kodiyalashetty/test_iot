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

#include "HpiSubProviderPower.h"


/************************************************
 * class cHpiSubProviderPower
 ***********************************************/
cHpiSubProviderPower::cHpiSubProviderPower()
    : cHpiSubProvider( eHpiEntryPower )
{
    // empty
}

cHpiSubProviderPower::~cHpiSubProviderPower()
{
    // empty
}

void cHpiSubProviderPower::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForPower( txt );
}

void cHpiSubProviderPower::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );

    SaErrorT rv;
    SaHpiPowerStateT state;

    rv = saHpiResourcePowerStateGet( m_ctx.session_id, m_ctx.resource_id, &state );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiResourcePowerStateGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"State", state );
}

void cHpiSubProviderPower::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderPower::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderPower::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderPower::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

