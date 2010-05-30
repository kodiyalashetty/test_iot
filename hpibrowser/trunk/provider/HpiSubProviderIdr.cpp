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

#include "HpiSubProviderIdr.h"


/************************************************
 * class cHpiSubProviderIdr
 ***********************************************/
cHpiSubProviderIdr::cHpiSubProviderIdr()
    : cHpiSubProvider( eHpiEntryIdr )
{
    // empty
}

cHpiSubProviderIdr::~cHpiSubProviderIdr()
{
    // empty
}

void cHpiSubProviderIdr::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForInstrument( SAHPI_INVENTORY_RDR, m_ctx.instrument_id, txt );
}

void cHpiSubProviderIdr::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;

    SaHpiRdrT rdr;
    rv = saHpiRdrGetByInstrumentId( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    SAHPI_INVENTORY_RDR,
                                    m_ctx.instrument_id,
                                    &rdr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiRdrGetByInstrumentId failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );
    Line( info, L"Entity", rdr.Entity );
    Line( info, L"IsFru", rdr.IsFru, UI8_SaHpiBool );

    const SaHpiInventoryRecT& ir = rdr.RdrTypeUnion.InventoryRec;

    Line( info, L"Idr Id", ir.IdrId, UI32_SaHpiIdrId );
    Line( info, L"Persistent", ir.Persistent, UI8_SaHpiBool );
    Line( info, L"OEM", ir.Oem );
    Line( info, L"IdString", rdr.IdString );

    SaHpiIdrInfoT idr_info;
    rv = saHpiIdrInfoGet( m_ctx.session_id,
                          m_ctx.resource_id,
                          m_ctx.instrument_id,
                          &idr_info );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiIdrInfoGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"Update Count", idr_info.UpdateCount );
    Line( info, L"Read Only", idr_info.ReadOnly, UI8_SaHpiBool );
    Line( info, L"Number of Areas", idr_info.NumAreas );
}

void cHpiSubProviderIdr::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderIdr::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderIdr::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;

    SaHpiEntryIdT id = SAHPI_FIRST_ENTRY, next_id;
    bool first = true;
    while( id != SAHPI_LAST_ENTRY ) {
        SaHpiIdrAreaHeaderT ahdr;
        rv = saHpiIdrAreaHeaderGet( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    m_ctx.instrument_id,
                                    SAHPI_IDR_AREATYPE_UNSPECIFIED,
                                    id,
                                    &next_id,
                                    &ahdr );
        if ( first && ( rv == SA_ERR_HPI_NOT_PRESENT ) ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForIdrArea( ahdr, name );
        entries.push_back( HpiEntry( eHpiEntryIdrArea, ahdr.AreaId, name ) );

        first = false;
        id = next_id;
    }
}

void cHpiSubProviderIdr::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if( short_entry.type != eHpiEntryIdrArea ) {
        return;
    }

    ctx         = m_ctx;
    ctx.type    = eHpiEntryIdrArea;
    ctx.area_id = short_entry.id;
}

