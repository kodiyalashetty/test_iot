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

#include "HpiSubProviderAnnunciator.h"


/************************************************
 * class cHpiSubProviderAnnunciator
 ***********************************************/
cHpiSubProviderAnnunciator::cHpiSubProviderAnnunciator()
    : cHpiSubProvider( eHpiEntryAnnunciator )
{
    // empty
}

cHpiSubProviderAnnunciator::~cHpiSubProviderAnnunciator()
{
    // empty
}

void cHpiSubProviderAnnunciator::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForInstrument( SAHPI_ANNUNCIATOR_RDR, m_ctx.instrument_id, txt );
}

void cHpiSubProviderAnnunciator::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;

    SaHpiRdrT rdr;
    rv = saHpiRdrGetByInstrumentId( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    SAHPI_ANNUNCIATOR_RDR,
                                    m_ctx.instrument_id,
                                    &rdr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiRdrGetByInstrumentId failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );
    Line( info, L"Entity", rdr.Entity );
    Line( info, L"IsFru", rdr.IsFru, UI8_SaHpiBool );

    const SaHpiAnnunciatorRecT& ar = rdr.RdrTypeUnion.AnnunciatorRec;

    Line( info, L"Annunciator Num", ar.AnnunciatorNum, UI32_SaHpiAnnunciatorNum );
    Line( info, L"Type", ar.AnnunciatorType );
    Line( info, L"Mode Read Only", ar.ModeReadOnly, UI8_SaHpiBool );
    Line( info, L"Max Conditions", ar.MaxConditions, UI32_AnnunciatorMaxConditions );
    Line( info, L"OEM", ar.Oem );
    Line( info, L"IdString", rdr.IdString );

    SaHpiAnnunciatorModeT mode;
    rv = saHpiAnnunciatorModeGet( m_ctx.session_id,
                                  m_ctx.resource_id,
                                  m_ctx.instrument_id,
                                  &mode );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiAnnunciatorModeGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"Mode", mode );
}

void cHpiSubProviderAnnunciator::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderAnnunciator::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderAnnunciator::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    SaErrorT rv;

    SaHpiAnnouncementT a;

    a.EntryId = SAHPI_FIRST_ENTRY;
    while( true ) {
        rv = saHpiAnnunciatorGetNext( m_ctx.session_id,
                                      m_ctx.resource_id,
                                      m_ctx.instrument_id,
                                      SAHPI_ALL_SEVERITIES,
                                      SAHPI_FALSE,
                                      &a );
        if( rv == SA_ERR_HPI_NOT_PRESENT ) {
            break;
        }

        if ( rv != SA_OK ) {
            return;
        }

        std::wstring name;
        MakeNameForAnnouncement( a, name );
        entries.push_back( HpiEntry( eHpiEntryAnnouncement, a.EntryId, name ) );
    }
}

void cHpiSubProviderAnnunciator::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if( short_entry.type != eHpiEntryAnnouncement ) {
        return;
    }

    ctx                 = m_ctx;
    ctx.type            = eHpiEntryAnnouncement;
    ctx.announcement_id = short_entry.id;
}

