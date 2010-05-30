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

#include "HpiSubProviderIdrField.h"


/************************************************
 * class cHpiSubProviderIdrField
 ***********************************************/
cHpiSubProviderIdrField::cHpiSubProviderIdrField()
    : cHpiSubProvider( eHpiEntryIdrField )
{
    // empty
}

cHpiSubProviderIdrField::~cHpiSubProviderIdrField()
{
    // empty
}

void cHpiSubProviderIdrField::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForIdrField( m_ctx.field_id, txt );
}

void cHpiSubProviderIdrField::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;
    SaHpiEntryIdT next_id;
    SaHpiIdrFieldT f;

    rv = saHpiIdrFieldGet( m_ctx.session_id,
                           m_ctx.resource_id,
                           m_ctx.instrument_id,
                           m_ctx.area_id,
                           SAHPI_IDR_FIELDTYPE_UNSPECIFIED,
                           m_ctx.field_id,
                           &next_id,
                           &f );
    if ( rv != SA_OK ) {
        return;
    }

    Line( info, L"Area Id", f.AreaId );
    Line( info, L"Field Id", f.FieldId );
    Line( info, L"Type", f.Type );
    Line( info, L"Read Only", f.ReadOnly, UI8_SaHpiBool );
    Line( info, L"Field Data", f.Field );
}

void cHpiSubProviderIdrField::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderIdrField::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderIdrField::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderIdrField::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

