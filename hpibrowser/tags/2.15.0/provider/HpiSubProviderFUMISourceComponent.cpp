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

#include "CommonHpiSubProviderFUMI.h"
#include "HpiSubProviderFUMISourceComponent.h"


/************************************************
 * class cHpiSubProviderFUMISourceComponent
 ***********************************************/
cHpiSubProviderFUMISourceComponent::cHpiSubProviderFUMISourceComponent()
    : cHpiSubProvider( eHpiEntryFUMISourceComponent )
{
    // empty
}

cHpiSubProviderFUMISourceComponent::~cHpiSubProviderFUMISourceComponent()
{
    // empty
}

void cHpiSubProviderFUMISourceComponent::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForFUMISourceComponent( m_ctx.source_component_id, txt );
}

void cHpiSubProviderFUMISourceComponent::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    // TODO bank id == bank num?
    Line( info, L"Bank Num", m_ctx.bank_num, UI8_SaHpiBankNum );

    SaHpiEntryIdT id = SAHPI_FIRST_ENTRY, next_id;
    SaHpiFumiComponentInfoT ci;
    bool found = false;

    while ( id != SAHPI_LAST_ENTRY ) {
        SaErrorT rv;
        rv = saHpiFumiSourceComponentInfoGet( m_ctx.session_id,
                                              m_ctx.resource_id,
                                              m_ctx.instrument_id,
                                              m_ctx.bank_num,
                                              id,
                                              &next_id,
                                              &ci );
        if ( rv != SA_OK ) {
            Line( info, L"saHpiFumiSourceComponentInfoGet failed", rv, I32_SaError );
            return;
        }

        if ( ci.ComponentId == m_ctx.component_id ) {
            found = true;
            break;
        }

        id = next_id;
    }
    if ( !found ) {
        Line( info, L"Component lookup failed", L"" );
        return;
    }

    Line( info, L"ComponentId", ci.ComponentId );
    GetFwInstanceInfo( L"Main Firmware Instance", ci.MainFwInstance, info );
    Line( info, L"Flags", ci.ComponentFlags );
}

void cHpiSubProviderFUMISourceComponent::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderFUMISourceComponent::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderFUMISourceComponent::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderFUMISourceComponent::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

