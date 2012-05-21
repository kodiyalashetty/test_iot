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

#include "HpiSubProviderLogEntry.h"


/************************************************
 * Event helpers
 ***********************************************/
static void GetEventDataInfo( const SaHpiResourceEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    Resource Event Type", ed.ResourceEventType );
}

static void GetEventDataInfo( const SaHpiDomainEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    Domain Event Type", ed.Type );
    Line( info, L"    Domain Id", ed.Type, UI32_SaHpiDomainId );
}

static void GetEventDataInfo( const SaHpiSensorEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    Sensor Num", ed.SensorNum, UI32_SaHpiSensorNum );
    Line( info, L"    Sensor Type", ed.SensorType );
    Line( info, L"    Event Category", ed.EventCategory );
    Line( info, L"    Assertion", ed.Assertion, UI8_SaHpiBool );
    Line( info, L"    Event State", ed.EventState, UI16_SaHpiEventState );
    Line( info, L"    Optional Data Present",
          ed.OptionalDataPresent,
          UI8_SaHpiSensorOptionalData );
    if ( ( ed.OptionalDataPresent & SAHPI_SOD_TRIGGER_READING ) != 0 ) {
        Line( info, L"    Trigger Reading", ed.TriggerReading );
    }
    if ( ( ed.OptionalDataPresent & SAHPI_SOD_TRIGGER_THRESHOLD ) != 0 ) {
        Line( info, L"    Trigger Threshold", ed.TriggerThreshold );
    }
    if ( ( ed.OptionalDataPresent & SAHPI_SOD_PREVIOUS_STATE ) != 0 ) {
        Line( info, L"    Previous State", ed.PreviousState, UI16_SaHpiEventState );
    }
    if ( ( ed.OptionalDataPresent & SAHPI_SOD_CURRENT_STATE ) != 0 ) {
        Line( info, L"    Current State", ed.CurrentState, UI16_SaHpiEventState );
    }
    if ( ( ed.OptionalDataPresent & SAHPI_SOD_OEM ) != 0 ) {
        Line( info, L"    Oem", ed.Oem );
    }
    if ( ( ed.OptionalDataPresent & SAHPI_SOD_SENSOR_SPECIFIC ) != 0 ) {
        Line( info, L"    Sensor Specific", ed.SensorSpecific );
    }
}

static void GetEventDataInfo( const SaHpiSensorEnableChangeEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    Sensor Num", ed.SensorNum, UI32_SaHpiSensorNum );
    Line( info, L"    Sensor Type", ed.SensorType );
    Line( info, L"    Event Category", ed.EventCategory );
    Line( info, L"    Sensor Enabled", ed.SensorEnable, UI8_SaHpiBool );
    Line( info, L"    Sensor Event Enabled", ed.SensorEventEnable, UI8_SaHpiBool );
    Line( info, L"    Assert Event Mask", ed.AssertEventMask, UI16_SaHpiEventState );
    Line( info, L"    Deassert Event Mask",
          ed.DeassertEventMask,
          UI16_SaHpiEventState );
    Line( info, L"    Optional Data Present",
          ed.OptionalDataPresent,
          UI8_SaHpiSensorEnableOptData );
    if ( ( ed.OptionalDataPresent & SAHPI_SEOD_CURRENT_STATE ) != 0 ) {
        Line( info, L"    Current State", ed.CurrentState, UI16_SaHpiEventState );
    }
    if ( ( ed.OptionalDataPresent & SAHPI_SEOD_ALARM_STATES ) != 0 ) {
        Line( info, L"    Critical Alarms",
              ed.CriticalAlarms,
              UI16_SaHpiEventState );
        Line( info, L"    Major Alarms",
              ed.MajorAlarms,
              UI16_SaHpiEventState );
        Line( info, L"    Minor Alarms",
              ed.MinorAlarms,
              UI16_SaHpiEventState );
    }
}

static void GetEventDataInfo( const SaHpiHotSwapEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    State", ed.HotSwapState );
    Line( info, L"    Previous State", ed.PreviousHotSwapState );
    Line( info, L"    Cause Of State Change", ed.CauseOfStateChange );
}

static void GetEventDataInfo( const SaHpiWatchdogEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    Watchdog Num", ed.WatchdogNum, UI32_SaHpiWatchdogNum );
    Line( info, L"    Action", ed.WatchdogAction );
    Line( info, L"    Pre-Timer Action", ed.WatchdogPreTimerAction );
    Line( info, L"    Action", ed.WatchdogAction );
    Line( info, L"    Timer Use", ed.WatchdogUse );
}

static void GetEventDataInfo( const SaHpiHpiSwEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    Manufacturer Id", ed.MId, UI32_SaHpiManufacturerId );
    Line( info, L"    Software Event Type", ed.Type );
    Line( info, L"    Software Event Data", ed.EventData );
}

static void GetEventDataInfo( const SaHpiOemEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    Manufacturer Id", ed.MId, UI32_SaHpiManufacturerId );
    Line( info, L"    OEM Event Data", ed.OemEventData );
}

static void GetEventDataInfo( const SaHpiUserEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    User Event Data", ed.UserEventData );
}

static void GetEventDataInfo( const SaHpiDimiEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    DIMI Num", ed.DimiNum, UI32_SaHpiDimiNum );
    Line( info, L"    Test Num", ed.TestNum, UI32_SaHpiDimiTestNum );
    Line( info, L"    Test Run Status", ed.DimiTestRunStatus );
    Line( info, L"    Percentage of Test Completed",
          ed.DimiTestPercentCompleted,
          UI8_SaHpiDimiTestPercentCompleted );
}

static void GetEventDataInfo( const SaHpiDimiUpdateEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    DIMI Num", ed.DimiNum, UI32_SaHpiDimiNum );
}

static void GetEventDataInfo( const SaHpiFumiEventT ed, std::deque<HpiInfo>& info )
{
    Line( info, L"    FUMI Num", ed.FumiNum, UI32_SaHpiFumiNum );
    Line( info, L"    Bank Num", ed.BankNum, UI8_SaHpiBankNum );
    Line( info, L"    Upgrade Status", ed.UpgradeStatus );
}

static void GetEventDataInfo( SaHpiEventTypeT type,
                              const SaHpiEventUnionT& eu,
                              std::deque<HpiInfo>& info )
{
    Line( info, L"  Event Data", L"" );
    switch ( type ) {
        case SAHPI_ET_RESOURCE:
            GetEventDataInfo( eu.ResourceEvent, info );
            return;
        case SAHPI_ET_DOMAIN:
            GetEventDataInfo( eu.DomainEvent, info );
            return;
        case SAHPI_ET_SENSOR:
            GetEventDataInfo( eu.SensorEvent, info );
            return;
        case SAHPI_ET_SENSOR_ENABLE_CHANGE:
            GetEventDataInfo( eu.SensorEnableChangeEvent, info );
            return;
        case SAHPI_ET_HOTSWAP:
            GetEventDataInfo( eu.HotSwapEvent, info );
            return;
        case SAHPI_ET_WATCHDOG:
            GetEventDataInfo( eu.WatchdogEvent, info );
            return;
        case SAHPI_ET_HPI_SW:
            GetEventDataInfo( eu.HpiSwEvent, info );
            return;
        case SAHPI_ET_OEM:
            GetEventDataInfo( eu.OemEvent, info );
            return;
        case SAHPI_ET_USER:
            GetEventDataInfo( eu.UserEvent, info );
            return;
        case SAHPI_ET_DIMI:
            GetEventDataInfo( eu.DimiEvent, info );
            return;
        case SAHPI_ET_DIMI_UPDATE:
            GetEventDataInfo( eu.DimiUpdateEvent, info );
            return;
        case SAHPI_ET_FUMI:
            GetEventDataInfo( eu.FumiEvent, info );
            return;
        default:
            break;
    }
}


/************************************************
 * class cHpiSubProviderLogEntry
 ***********************************************/
cHpiSubProviderLogEntry::cHpiSubProviderLogEntry()
    : cHpiSubProvider( eHpiEntryLogEntry )
{
    // empty
}

cHpiSubProviderLogEntry::~cHpiSubProviderLogEntry()
{
    // empty
}

void cHpiSubProviderLogEntry::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForLogEntry( m_ctx.log_entry_id, txt );
}

void cHpiSubProviderLogEntry::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiEventLogEntryIdT prev_id, next_id;
    SaHpiEventLogEntryT elentry;
    SaHpiRdrT rdr;
    SaHpiRptEntryT rpte;

    rv = saHpiEventLogEntryGet( m_ctx.session_id,
                                m_ctx.resource_id,
                                m_ctx.log_entry_id,
                                &prev_id,
                                &next_id,
                                &elentry,
                                &rdr,
                                &rpte );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiEventLogEntryGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Entry Id", elentry.EntryId, UI32_SaHpiEventLogEntryId );
    Line( info, L"Timestamp", elentry.Timestamp, I64_SaHpiTime );

    const SaHpiEventT& e = elentry.Event;
    Line( info, L"Event", L"" );
    Line( info, L"  Source Resource", e.Source, UI32_SaHpiResourceId );
    Line( info, L"  Event Type", e.EventType );
    Line( info, L"  Timestamp", e.Timestamp, I64_SaHpiTime );
    Line( info, L"  Severity", e.Severity );
    GetEventDataInfo( e.EventType, e.EventDataUnion, info );

    // TODO rdr, rpte
}

void cHpiSubProviderLogEntry::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderLogEntry::ExecuteAction( const HpiActionShort& )
{
}

void cHpiSubProviderLogEntry::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderLogEntry::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

