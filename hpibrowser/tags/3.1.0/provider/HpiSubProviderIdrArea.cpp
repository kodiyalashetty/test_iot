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

#include "HpiSubProviderIdrArea.h"


/************************************************
 * class cHpiSubProviderIdrArea
 ***********************************************/
cHpiSubProviderIdrArea::cHpiSubProviderIdrArea()
    : cHpiSubProvider( eHpiEntryIdrArea )
{
    // empty
}

cHpiSubProviderIdrArea::~cHpiSubProviderIdrArea()
{
    // empty
}

void cHpiSubProviderIdrArea::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForIdrArea( m_ctx.area_id, txt );
}

void cHpiSubProviderIdrArea::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiEntryIdT next_id;
    SaHpiIdrAreaHeaderT ahdr;
    rv = saHpiIdrAreaHeaderGet( m_ctx.session_id,
                                m_ctx.resource_id,
                                m_ctx.instrument_id,
                                SAHPI_IDR_AREATYPE_UNSPECIFIED,
                                m_ctx.area_id,
                                &next_id,
                                &ahdr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiIdrAreaHeaderGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Idr Id", m_ctx.instrument_id, UI32_SaHpiIdrId );
    Line( info, L"Area Id", ahdr.AreaId );
    Line( info, L"Type", ahdr.Type );
    Line( info, L"Read Only", ahdr.ReadOnly, UI8_SaHpiBool );
    Line( info, L"Number of Fields", ahdr.NumFields );
}

void cHpiSubProviderIdrArea::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderIdrArea::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderIdrArea::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;


    SaHpiEntryIdT id = SAHPI_FIRST_ENTRY, next_id;
    bool first = true;
    while( id != SAHPI_LAST_ENTRY ) {
        SaHpiIdrFieldT f;
        rv = saHpiIdrFieldGet( m_ctx.session_id,
                               m_ctx.resource_id,
                               m_ctx.instrument_id,
                               m_ctx.area_id,
                               SAHPI_IDR_FIELDTYPE_UNSPECIFIED,
                               id,
                               &next_id,
                               &f );
        if( first && ( rv == SA_ERR_HPI_NOT_PRESENT ) ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForIdrField( f, name );
        entries.push_back( HpiEntry( eHpiEntryIdrField, f.FieldId, name ) );

        first = false;
        id = next_id;
    }
}

void cHpiSubProviderIdrArea::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if( short_entry.type != eHpiEntryIdrField ) {
        return;
    }

    ctx          = m_ctx;
    ctx.type     = eHpiEntryIdrField;
    ctx.field_id = short_entry.id;
}

