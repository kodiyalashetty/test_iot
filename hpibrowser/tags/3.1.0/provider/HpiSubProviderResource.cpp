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

#include "HpiSubProviderResource.h"


/************************************************
 * class cHpiSubProviderResource
 ***********************************************/
cHpiSubProviderResource::cHpiSubProviderResource()
    : cHpiSubProvider( eHpiEntryResource )
{
    // empty
}

cHpiSubProviderResource::~cHpiSubProviderResource()
{
    // empty
}

void cHpiSubProviderResource::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForResource( m_ctx.resource_id, txt );
}

void cHpiSubProviderResource::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiRptEntryT rpte;

    rv = saHpiRptEntryGetByResourceId( m_ctx.session_id, m_ctx.resource_id, &rpte );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiRptEntryGetByResourceIdt failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Resource Id", rpte.ResourceId, UI32_SaHpiResourceId );

    const SaHpiResourceInfoT& rinfo = rpte.ResourceInfo;

    Line( info, L"Resource Info", L"" );
    Line( info, L"  Revision", rinfo.ResourceRev );
    Line( info, L"  Specific Version", rinfo.SpecificVer );
    Line( info, L"  Device Support", rinfo.DeviceSupport );
    Line( info, L"  Manufacturer Id", rinfo.ManufacturerId, UI32_SaHpiManufacturerId );
    Line( info, L"  Product Id", rinfo.ProductId );
    FirmwareRevision fw( rinfo.FirmwareMajorRev, rinfo.FirmwareMinorRev, rinfo.AuxFirmwareRev );
    Line( info, L"  Firmware Revision", fw );
    Line( info, L"  GUID",  rinfo.Guid );
    Line( info, L"Entity", rpte.ResourceEntity );
    Line( info, L"Capabilities", rpte.ResourceCapabilities, UI32_SaHpiCapabilities );
    Line( info, L"Hot Swap Capabilities",
                             rpte.HotSwapCapabilities,
                             UI32_SaHpiHsCapabilities );
    Line( info, L"Severity", rpte.ResourceSeverity );
    Line( info, L"Is Failed", rpte.ResourceFailed, UI8_SaHpiBool );
    Line( info, L"Tag", rpte.ResourceTag );
}


void cHpiSubProviderResource::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
    // TODO parm control, load id
}

void cHpiSubProviderResource::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderResource::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;
    SaHpiRptEntryT rpte;
    rv = saHpiRptEntryGetByResourceId( m_ctx.session_id, m_ctx.resource_id, &rpte );
    if ( rv != SA_OK ) {
        return;
    }

    std::wstring name;
    if ( ( rpte.ResourceCapabilities & SAHPI_CAPABILITY_EVENT_LOG ) != 0 ) {
        MakeNameForLog( m_ctx.resource_id, name );
        entries.push_back( HpiEntry( eHpiEntryLog, 0, name ) );
    }
    if ( ( rpte.ResourceCapabilities & SAHPI_CAPABILITY_MANAGED_HOTSWAP ) != 0 ) {
        MakeNameForHotSwap( name );
        entries.push_back( HpiEntry( eHpiEntryHotSwap, 0, name ) );
    }
    if ( ( rpte.ResourceCapabilities & SAHPI_CAPABILITY_RESET ) != 0 ) {
        MakeNameForReset( name );
        entries.push_back( HpiEntry( eHpiEntryReset, 0, name ) );
    }
    if ( ( rpte.ResourceCapabilities & SAHPI_CAPABILITY_POWER ) != 0 ) {
        MakeNameForPower( name );
        entries.push_back( HpiEntry( eHpiEntryPower, 0, name ) );
    }

    GetInstrumentEntries( entries );
}

void cHpiSubProviderResource::GetEntryCtx( const HpiEntryShort& short_entry,
                                           HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    switch ( short_entry.type ) {
        case eHpiEntryLog:
        case eHpiEntryHotSwap:
        case eHpiEntryReset:
        case eHpiEntryPower:
            ctx      = m_ctx;
            ctx.type = short_entry.type;
            return;
        default:
            break;
    }

    SaHpiRdrTypeT rdr_type = EntryType2RdrType( short_entry.type );
    if ( rdr_type == SAHPI_NO_RECORD ) {
        return;
    }

    ctx               = m_ctx;
    ctx.type          = short_entry.type;
    ctx.instrument_id = short_entry.id;
}

void cHpiSubProviderResource::GetInstrumentEntries( std::deque<HpiEntry>& entries ) const
{
    SaErrorT rv;
    SaHpiRdrT rdr;
    SaHpiEntryIdT id = SAHPI_FIRST_ENTRY, next_id;
    bool first = true;
    while ( id != SAHPI_LAST_ENTRY ) {
        rv = saHpiRdrGet( m_ctx.session_id, m_ctx.resource_id, id, &next_id, &rdr );
        if ( first && ( rv == SA_ERR_HPI_NOT_PRESENT ) ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForInstrument( rdr, name );
        SaHpiInstrumentIdT instr_id = GetInstrumentId( rdr );
        entries.push_back( HpiEntry( RdrType2EntryType( rdr.RdrType ), instr_id, name ) );

        first = false;
        id = next_id;
    }
}
