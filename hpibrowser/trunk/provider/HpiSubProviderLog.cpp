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

#include "HpiSubProviderLog.h"


/************************************************
 * class cHpiSubProviderLog
 ***********************************************/
cHpiSubProviderLog::cHpiSubProviderLog()
    : cHpiSubProvider( eHpiEntryLog )
{
    // empty
}

cHpiSubProviderLog::~cHpiSubProviderLog()
{
    // empty
}

void cHpiSubProviderLog::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForLog( m_ctx.resource_id, txt );
}

void cHpiSubProviderLog::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiEventLogInfoT elinfo;
    SaHpiEventLogCapabilitiesT elcaps;

    rv = saHpiEventLogInfoGet( m_ctx.session_id, m_ctx.resource_id, &elinfo );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiEventLogInfoGet failed", rv, I32_SaError );
        return;
    }

    if ( m_ctx.resource_id == SAHPI_UNSPECIFIED_RESOURCE_ID ) {
        Line( info, L"Domain Id", m_ctx.domain_id, UI32_SaHpiDomainId );
    } else {
        Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );
    }
    Line( info, L"Entries", elinfo.Entries );
    Line( info, L"Size", elinfo.Size );
    Line( info, L"Max Size of User Event Data, bytes", elinfo.UserEventMaxSize );
    Line( info, L"Update Timestamp", elinfo.UpdateTimestamp, I64_SaHpiTime );
    Line( info, L"Current Time", elinfo.CurrentTime, I64_SaHpiTime );
    Line( info, L"Enabled", elinfo.Enabled, UI8_SaHpiBool );
    Line( info, L"Overflow Flag", elinfo.OverflowFlag, UI8_SaHpiBool );
    Line( info, L"Overflow Resetable", elinfo.OverflowResetable, UI8_SaHpiBool );
    Line( info, L"Overflow Action", elinfo.OverflowAction );

    rv = saHpiEventLogCapabilitiesGet( m_ctx.session_id, m_ctx.resource_id, &elcaps );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiEventLogCapabilitiesGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Capabilities", elcaps, UI32_SaHpiEventLogCapabilities );
}

void cHpiSubProviderLog::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderLog::ExecuteAction( const HpiActionShort& )
{
}

void cHpiSubProviderLog::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;
    SaHpiEventLogEntryIdT id, prev_id, next_id;
    SaHpiEventLogEntryT elentry;
    SaHpiRdrT rdr;
    SaHpiRptEntryT rpte;

    bool first = true;
    id = SAHPI_OLDEST_ENTRY;
    while( id != SAHPI_NO_MORE_ENTRIES ) {
        rv = saHpiEventLogEntryGet( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    id,
                                    &prev_id,
                                    &next_id,
                                    &elentry,
                                    &rdr,
                                    &rpte );
        if ( first && ( rv == SA_ERR_HPI_NOT_PRESENT ) ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForLogEntry( elentry, name );
        entries.push_back( HpiEntry( eHpiEntryLogEntry, elentry.EntryId, name ) );

        first = false;
        id = next_id;
    }
}

void cHpiSubProviderLog::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if ( short_entry.type != eHpiEntryLogEntry ) {
        return;
    }

    ctx              = m_ctx;
    ctx.type         = eHpiEntryLogEntry;
    ctx.log_entry_id = short_entry.id;
}

