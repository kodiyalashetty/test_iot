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

#include "HpiSubProviderSensor.h"


/************************************************
 * class cHpiSubProviderSensor
 ***********************************************/
cHpiSubProviderSensor::cHpiSubProviderSensor()
    : cHpiSubProvider( eHpiEntrySensor )
{
    // empty
}

cHpiSubProviderSensor::~cHpiSubProviderSensor()
{
    // empty
}

void cHpiSubProviderSensor::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForInstrument( SAHPI_SENSOR_RDR, m_ctx.instrument_id, txt );
}


void cHpiSubProviderSensor::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiRdrT rdr;

    rv = saHpiRdrGetByInstrumentId( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    SAHPI_SENSOR_RDR,
                                    m_ctx.instrument_id,
                                    &rdr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiRdrGetByInstrumentId failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );
    Line( info, L"Entity", rdr.Entity );
    Line( info, L"Is Fru", rdr.IsFru, UI8_SaHpiBool );

    const SaHpiSensorRecT& sr = rdr.RdrTypeUnion.SensorRec;

    Line( info, L"Sensor Num", sr.Num, UI32_SaHpiSensorNum );
    Line( info, L"Type", sr.Type );
    Line( info, L"Category", sr.Category, UI8_SaHpiEventCategory );
    Line( info, L"Enable Control", sr.EnableCtrl, UI8_SaHpiBool );
    Line( info, L"Event Control", sr.EventCtrl );
    Line( info, L"Events", sr.Events, UI16_SaHpiEventState );

    const SaHpiSensorDataFormatT& df = sr.DataFormat;
    if ( df.IsSupported != SAHPI_FALSE ) {

        Line( info, L"Data Format", L"" );
        Line( info, L"  Reading Type", df.ReadingType );
        Line( info, L"  Base Units", df.BaseUnits );
        Line( info, L"  Modifier Units", df.ModifierUnits );
        Line( info, L"  Modifier Use", df.ModifierUse );
        Line( info, L"  Percentage", df.Percentage, UI8_SaHpiBool );

        const SaHpiSensorRangeT& range = df.Range;

        Line( info, L"  Range", L"" );
        Line( info, L"    Flags", range.Flags, UI8_SaHpiSensorRangeFlags );
        if ( ( range.Flags & SAHPI_SRF_MAX ) != 0 ) {
            Line( info, L"    Max", range.Max );
        }
        if ( ( range.Flags & SAHPI_SRF_MIN ) != 0 ) {
            Line( info, L"    Min", range.Min );
        }
        if ( ( range.Flags & SAHPI_SRF_NOMINAL ) != 0 ) {
            Line( info, L"    Nominal", range.Nominal );
        }
        if ( ( range.Flags & SAHPI_SRF_NORMAL_MAX) != 0 ) {
            Line( info, L"    Normal Max", range.NormalMax );
        }
        if ( ( range.Flags & SAHPI_SRF_NORMAL_MIN ) != 0 ) {
            Line( info, L"    Normal Min", range.NormalMin );
        }
        Line( info, L"  Accuracy Factor", df.AccuracyFactor );
    }

    const SaHpiSensorThdDefnT& thd = sr.ThresholdDefn;
    if ( thd.IsAccessible != SAHPI_FALSE ) {
        Line( info, L"  Threshold Definition", L"" );
        Line( info, L"  Readable Thresholds", thd.ReadThold, UI8_SaHpiSensorThdMask );
        Line( info, L"  Writable Thresholds", thd.WriteThold, UI8_SaHpiSensorThdMask );
        Line( info, L"  Nonlinear", thd.Nonlinear, UI8_SaHpiBool );
    }

    Line( info, L"OEM", sr.Oem );
    Line( info, L"Id String", rdr.IdString );

    Line( info, L"Current State", L"" );

    SaHpiBoolT enabled;
    rv = saHpiSensorEnableGet( m_ctx.session_id,
                               m_ctx.resource_id,
                               m_ctx.instrument_id,
                               &enabled );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiSensorEnableGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"  Enabled", enabled, UI8_SaHpiBool );

    SaHpiBoolT event_enabled;
    rv = saHpiSensorEventEnableGet( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    m_ctx.instrument_id,
                                    &event_enabled );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiSensorEventEnableGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"  Event Enabled", event_enabled, UI8_SaHpiBool );

    if ( enabled != SAHPI_FALSE ) {
        SaHpiSensorReadingT reading;
        SaHpiEventStateT state;
        rv = saHpiSensorReadingGet( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    m_ctx.instrument_id,
                                    &reading,
                                    &state );
        if ( rv != SA_OK ) {
            Line( info, L"saHpiSensorReadingGet failed", rv, I32_SaError );
            return;
        }
        Line( info, L"  Reading", reading );
        Line( info, L"  Event State", state, UI16_SaHpiEventState );
    }

    SaHpiEventStateT amask, dmask;
    rv = saHpiSensorEventMasksGet( m_ctx.session_id,
                                   m_ctx.resource_id,
                                   m_ctx.instrument_id,
                                   &amask,
                                   &dmask );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiSensorEventMasksGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"  Assert Event Mask", amask, UI16_SaHpiEventState );
    Line( info, L"  Deassert Event Mask", dmask, UI16_SaHpiEventState );

    if ( ( sr.Category == SAHPI_EC_THRESHOLD ) && ( thd.ReadThold != 0 ) ) {
        SaHpiSensorThresholdsT ths;
        rv = saHpiSensorThresholdsGet( m_ctx.session_id,
                                       m_ctx.resource_id,
                                       m_ctx.instrument_id,
                                       &ths );
        if ( rv != SA_OK ) {
            Line( info, L"saHpiSensorThresholdsGet failed", rv, I32_SaError );
            return;
        }
        Line( info, L"  Thresholds", L"" );
        if ( (thd.ReadThold & SAHPI_STM_LOW_CRIT ) != 0 ) {
            Line( info, L"     Lower Critical", ths.LowCritical );
        }
        if ( (thd.ReadThold & SAHPI_STM_LOW_MAJOR ) != 0 ) {
            Line( info, L"     Lower Major", ths.LowMajor );
        }
        if ( (thd.ReadThold & SAHPI_STM_LOW_MINOR ) != 0 ) {
            Line( info, L"     Lower Minor", ths.LowMinor );
        }
        if ( (thd.ReadThold & SAHPI_STM_UP_MINOR ) != 0 ) {
            Line( info, L"     Upper Minor", ths.UpMinor );
        }
        if ( (thd.ReadThold & SAHPI_STM_UP_MAJOR ) != 0 ) {
            Line( info, L"     Upper Major", ths.UpMajor );
        }
        if ( (thd.ReadThold & SAHPI_STM_UP_CRIT ) != 0 ) {
            Line( info, L"     Upper Critical", ths.UpCritical );
        }
        if ( (thd.ReadThold & SAHPI_STM_UP_HYSTERESIS ) != 0 ) {
            Line( info, L"     Positive Hysteresis", ths.PosThdHysteresis );
        }
        if ( (thd.ReadThold & SAHPI_STM_LOW_HYSTERESIS ) != 0 ) {
            Line( info, L"     Negative Hysteresis", ths.NegThdHysteresis );
        }
    }
}

void cHpiSubProviderSensor::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderSensor::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderSensor::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderSensor::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

