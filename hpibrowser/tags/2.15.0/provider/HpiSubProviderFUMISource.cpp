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
#include "HpiSubProviderFUMISource.h"


/************************************************
 * class cHpiSubProviderFUMISource
 ***********************************************/
cHpiSubProviderFUMISource::cHpiSubProviderFUMISource()
    : cHpiSubProvider( eHpiEntryFUMISource )
{
    // empty
}

cHpiSubProviderFUMISource::~cHpiSubProviderFUMISource()
{
    // empty
}

void cHpiSubProviderFUMISource::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForFUMISource( txt );
}

void cHpiSubProviderFUMISource::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiFumiSourceInfoT si;

    rv = saHpiFumiSourceInfoGet( m_ctx.session_id,
                                 m_ctx.resource_id,
                                 m_ctx.instrument_id,
                                 m_ctx.bank_num,
                                 &si );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiFumiSourceInfoGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Bank Num", m_ctx.bank_num, UI8_SaHpiBankNum );
    Line( info, L"Source URI", si.SourceUri );
    Line( info, L"Identifier", si.Identifier );
    Line( info, L"Description", si.Description );
    Line( info, L"Firmware Build Date-Time", si.DateTime );
    FirmwareRevision fw( si.MajorVersion, si.MinorVersion, si.AuxVersion );
    Line( info, L"Firmware Revision", fw );
}

void cHpiSubProviderFUMISource::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderFUMISource::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderFUMISource::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;
    SaHpiRdrT rdr;

    rv = saHpiRdrGetByInstrumentId( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    SAHPI_FUMI_RDR,
                                    m_ctx.instrument_id,
                                    &rdr );
    if ( rv != SA_OK ) {
        return;
    }

    SaHpiFumiCapabilityT caps = rdr.RdrTypeUnion.FumiRec.Capability;
    if ( ( caps & SAHPI_FUMI_CAP_COMPONENTS ) == 0 ) {
        return;
    }

    SaHpiEntryIdT id, next_id;
    SaHpiFumiComponentInfoT ci;

    bool first = true;
    id = SAHPI_FIRST_ENTRY;
    while ( id != SAHPI_LAST_ENTRY ) {
        rv = saHpiFumiSourceComponentInfoGet( m_ctx.session_id,
                                              m_ctx.resource_id,
                                              m_ctx.instrument_id,
                                              m_ctx.bank_num,
                                              id,
                                              &next_id,
                                              &ci );
        if ( first && ( rv == SA_ERR_HPI_NOT_PRESENT ) ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForFUMISourceComponent( ci, name );
        entries.push_back( HpiEntry( eHpiEntryFUMISourceComponent, ci.ComponentId, name ) );

        first = false;
        id = next_id;
    }
}

void cHpiSubProviderFUMISource::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if( short_entry.type != eHpiEntryFUMISourceComponent ) {
        return;
    }

    ctx                     = m_ctx;
    ctx.type                = eHpiEntryFUMISourceComponent;
    ctx.source_component_id = short_entry.id;
}

