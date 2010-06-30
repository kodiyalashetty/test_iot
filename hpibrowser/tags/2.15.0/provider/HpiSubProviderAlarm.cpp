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

#include "HpiSubProviderAlarm.h"


/************************************************
 * class cHpiSubProviderAlarm
 ***********************************************/
cHpiSubProviderAlarm::cHpiSubProviderAlarm()
    : cHpiSubProvider( eHpiEntryAlarm )
{
    // empty
}

cHpiSubProviderAlarm::~cHpiSubProviderAlarm()
{
    // empty
}

void cHpiSubProviderAlarm::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForAlarm( m_ctx.alarm_id, txt );
}

void cHpiSubProviderAlarm::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiAlarmT a;

    rv = saHpiAlarmGet( m_ctx.session_id, m_ctx.alarm_id, &a );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiAlarmGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Alarm Id", a.AlarmId, UI32_SaHpiAlarmId );
    Line( info, L"Timestamp", a.Timestamp, I64_SaHpiTime );
    Line( info, L"Severity", a.Severity );
    Line( info, L"Acknowledged", a.Acknowledged, UI8_SaHpiBool );

    const SaHpiConditionT& c = a.AlarmCond;

    Line( info, L"Condition", L"" );
    Line( info, L"  Type", c.Type );
    Line( info, L"  Entity", c.Entity );
    Line( info, L"  Domain Id", c.DomainId, UI32_ConditionDomainId );
    Line( info, L"  Resource Id", c.ResourceId, UI32_SaHpiResourceId );
    if ( c.Type == SAHPI_STATUS_COND_TYPE_SENSOR ) {
        Line( info, L"  Sensor Number", c.SensorNum, UI32_SaHpiSensorNum );
        Line( info, L"  Event State", c.EventState, UI16_SaHpiEventState );
    }
    Line( info, L"  Name", c.Name );
    if ( c.Type == SAHPI_STATUS_COND_TYPE_OEM ) {
        Line( info, L"  Manufacturer Id", c.Mid, UI32_SaHpiManufacturerId );
    }
    Line( info, L"  Data", c.Data );
}


void cHpiSubProviderAlarm::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderAlarm::ExecuteAction( const HpiActionShort& )
{
}

void cHpiSubProviderAlarm::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderAlarm::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

