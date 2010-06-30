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

#include "HpiSubProviderHotSwap.h"


/************************************************
 * class cHpiSubProviderHotSwap
 ***********************************************/
cHpiSubProviderHotSwap::cHpiSubProviderHotSwap()
    : cHpiSubProvider( eHpiEntryHotSwap )
{
    // empty
}

cHpiSubProviderHotSwap::~cHpiSubProviderHotSwap()
{
    // empty
}

void cHpiSubProviderHotSwap::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForHotSwap( txt );
}

void cHpiSubProviderHotSwap::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );

    SaErrorT rv;

    SaHpiHsStateT state;
    rv = saHpiHotSwapStateGet( m_ctx.session_id, m_ctx.resource_id, &state );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiHotSwapStateGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"State", state );

    SaHpiHsIndicatorStateT indicator_state;
    rv = saHpiHotSwapIndicatorStateGet( m_ctx.session_id, m_ctx.resource_id, &indicator_state );
    if ( rv == SA_OK ) {
        Line( info, L"Indicator State", indicator_state );
    } else if ( rv == SA_ERR_HPI_CAPABILITY ) {
        // hot swap indicator not supported, do nothing
    } else {
        Line( info, L"saHpiHotSwapIndicatorStateGet failed", rv, I32_SaError );
        return;
    }

    SaHpiTimeoutT aet;
    rv = saHpiAutoExtractTimeoutGet( m_ctx.session_id, m_ctx.resource_id, &aet );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiAutoExtractTimeoutGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"Auto-Extraction Timeout, ns", aet, I64_SaHpiTimeout );
}

void cHpiSubProviderHotSwap::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderHotSwap::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderHotSwap::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderHotSwap::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}
