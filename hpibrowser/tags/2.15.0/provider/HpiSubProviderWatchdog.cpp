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

#include "HpiSubProviderWatchdog.h"


/************************************************
 * class cHpiSubProviderWatchdog
 ***********************************************/
cHpiSubProviderWatchdog::cHpiSubProviderWatchdog()
    : cHpiSubProvider( eHpiEntryWatchdog )
{
    // empty
}

cHpiSubProviderWatchdog::~cHpiSubProviderWatchdog()
{
    // empty
}

void cHpiSubProviderWatchdog::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForInstrument( SAHPI_WATCHDOG_RDR, m_ctx.instrument_id, txt );
}

void cHpiSubProviderWatchdog::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiRdrT rdr;
    rv = saHpiRdrGetByInstrumentId( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    SAHPI_WATCHDOG_RDR,
                                    m_ctx.instrument_id,
                                    &rdr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiRdrGetByInstrumentId failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );
    Line( info, L"Entity", rdr.Entity );
    Line( info, L"IsFru", rdr.IsFru, UI8_SaHpiBool );

    const SaHpiWatchdogRecT& wr = rdr.RdrTypeUnion.WatchdogRec;

    Line( info, L"Watchdog Num", wr.WatchdogNum, UI32_SaHpiWatchdogNum );
    Line( info, L"OEM", wr.Oem );
    Line( info, L"IdString", rdr.IdString );

    SaHpiWatchdogT w;
    rv = saHpiWatchdogTimerGet( m_ctx.session_id,
                                m_ctx.resource_id,
                                m_ctx.instrument_id,
                                &w );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiWatchdogTimerGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Current Settings and Configuration", L"" );
    Line( info, L"  Log", w.Log, UI8_SaHpiBool );
    Line( info, L"  Running", w.Running, UI8_SaHpiBool );
    Line( info, L"  Timer Use", w.TimerUse );
    Line( info, L"  Timer Action", w.TimerAction );
    Line( info, L"  Pre-Timer Interrupt", w.PretimerInterrupt );
    Line( info, L"  Pre-Timeout Interval, ms", w.PreTimeoutInterval );
    Line( info, L"  Timer Use Expiration Flags",
          w.TimerUseExpFlags,
          UI8_SaHpiWatchdogExpFlags );
    Line( info, L"  Initial Count", w.InitialCount );
    Line( info, L"  Present Count", w.PresentCount );
}

void cHpiSubProviderWatchdog::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderWatchdog::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderWatchdog::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderWatchdog::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

