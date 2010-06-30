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

#include "HpiSubProviderDIMI.h"


/************************************************
 * class cHpiSubProviderDIMI
 ***********************************************/
cHpiSubProviderDIMI::cHpiSubProviderDIMI()
    : cHpiSubProvider( eHpiEntryDIMI )
{
    // empty
}

cHpiSubProviderDIMI::~cHpiSubProviderDIMI()
{
    // empty
}

void cHpiSubProviderDIMI::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForInstrument( SAHPI_DIMI_RDR, m_ctx.instrument_id, txt );
}

void cHpiSubProviderDIMI::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;

    SaHpiRdrT rdr;
    rv = saHpiRdrGetByInstrumentId( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    SAHPI_DIMI_RDR,
                                    m_ctx.instrument_id,
                                    &rdr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiRdrGetByInstrumentId failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );
    Line( info, L"Entity", rdr.Entity );
    Line( info, L"IsFru", rdr.IsFru, UI8_SaHpiBool );

    const SaHpiDimiRecT& dr = rdr.RdrTypeUnion.DimiRec;

    Line( info, L"DIMI Num", dr.DimiNum, UI32_SaHpiDimiNum );
    Line( info, L"OEM", dr.Oem );
    Line( info, L"IdString", rdr.IdString );

    SaHpiDimiInfoT di;
    rv = saHpiDimiInfoGet( m_ctx.session_id,
                           m_ctx.resource_id,
                           m_ctx.instrument_id,
                           &di );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiDimiInfoGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"Number of Tests", di.NumberOfTests );
    Line( info, L"Test Number Update Counter", di.TestNumUpdateCounter );
}

void cHpiSubProviderDIMI::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderDIMI::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderDIMI::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;

    SaHpiDimiInfoT di;
    rv = saHpiDimiInfoGet( m_ctx.session_id,
                           m_ctx.resource_id,
                           m_ctx.instrument_id,
                           &di );
    if ( rv != SA_OK ) {
        return;
    }

    for ( SaHpiDimiTestNumT tnum = 0; tnum < di.NumberOfTests; ++tnum ) {
        SaHpiDimiTestT dti;

        rv = saHpiDimiTestInfoGet( m_ctx.session_id,
                                   m_ctx.resource_id,
                                   m_ctx.instrument_id,
                                   tnum,
                                   &dti );
        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForDIMITest( tnum, dti, name );
        entries.push_back( HpiEntry( eHpiEntryDIMITest, tnum, name ) );
    }
}

void cHpiSubProviderDIMI::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if( short_entry.type != eHpiEntryDIMITest ) {
        return;
    }

    ctx          = m_ctx;
    ctx.type     = eHpiEntryDIMITest;
    ctx.test_num = short_entry.id;
}

