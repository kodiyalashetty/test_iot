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

#include "HpiSubProviderDAT.h"


/************************************************
 * class cHpiSubProviderDAT
 ***********************************************/
cHpiSubProviderDAT::cHpiSubProviderDAT()
    : cHpiSubProvider( eHpiEntryDAT )
{
    // empty
}

cHpiSubProviderDAT::~cHpiSubProviderDAT()
{
    // empty
}

void cHpiSubProviderDAT::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForDAT( txt );
}

void cHpiSubProviderDAT::GetInfo( std::deque<HpiInfo>& info ) const
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
    Line( info, L"Update Count", di.DatUpdateCount );
    Line( info, L"Update Timestamp", di.DatUpdateTimestamp, I64_SaHpiTime );
    Line( info, L"Active Alarms", di.ActiveAlarms );
    Line( info, L"Critical Alarms", di.CriticalAlarms );
    Line( info, L"Major Alarms", di.MajorAlarms );
    Line( info, L"Minor Alarms", di.MinorAlarms );
    Line( info, L"User Alarm Limit", di.DatUserAlarmLimit, UI32_DatUserAlarmLimit );
    Line( info, L"Overflow Flag", di.DatOverflow, UI8_SaHpiBool );
}

void cHpiSubProviderDAT::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderDAT::ExecuteAction( const HpiActionShort& )
{
}

void cHpiSubProviderDAT::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;
    SaHpiAlarmT a;

    a.AlarmId = SAHPI_FIRST_ENTRY;
    while ( true ) {
        rv = saHpiAlarmGetNext( m_ctx.session_id, SAHPI_ALL_SEVERITIES, SAHPI_FALSE, &a );
        if ( rv == SA_ERR_HPI_NOT_PRESENT ) {
            break;
        }
        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForAlarm( a, name );
        entries.push_back( HpiEntry( eHpiEntryAlarm, a.AlarmId, name ) );
    }
}

void cHpiSubProviderDAT::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if ( short_entry.type != eHpiEntryAlarm ) {
        return;
    }

    ctx          = m_ctx;
    ctx.type     = eHpiEntryAlarm;
    ctx.alarm_id = short_entry.id;
}

