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

#include "HpiSubProviderEntity.h"


/************************************************
 * class HpiSubProviderEntity
 ***********************************************/
cHpiSubProviderEntity::cHpiSubProviderEntity()
    : cHpiSubProvider( eHpiEntryEntity )
{
    // empty
}

cHpiSubProviderEntity::~cHpiSubProviderEntity()
{
    // empty
}

void cHpiSubProviderEntity::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForEntity( txt );
}

void cHpiSubProviderEntity::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();
    Line( info, L"Entity Path", m_ctx.entity_path );
}

void cHpiSubProviderEntity::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderEntity::ExecuteAction( const HpiActionShort& )
{
}

void cHpiSubProviderEntity::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    GetEntityEntries( entries );
    GetResourceEntries( entries );
    GetInstrumentEntries( SAHPI_CTRL_RDR, entries );
    GetInstrumentEntries( SAHPI_SENSOR_RDR, entries );
    GetInstrumentEntries( SAHPI_INVENTORY_RDR, entries );
    GetInstrumentEntries( SAHPI_WATCHDOG_RDR, entries );
    GetInstrumentEntries( SAHPI_ANNUNCIATOR_RDR, entries );
    GetInstrumentEntries( SAHPI_DIMI_RDR, entries );
    GetInstrumentEntries( SAHPI_FUMI_RDR, entries );
}

void cHpiSubProviderEntity::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if ( short_entry.type == eHpiEntryEntity ) {
        GetEntityEntryCtx( short_entry.id, ctx );
        return;
    } else if ( short_entry.type == eHpiEntryResource ) {
        GetResourceEntryCtx( short_entry.id, ctx );
        return;
    } else {
        SaHpiRdrTypeT type = EntryType2RdrType( short_entry.type );
        if ( type == SAHPI_NO_RECORD ) {
            return;
        }
        GetInstrumentEntryCtx( type, short_entry.id, ctx );
    }
}

void cHpiSubProviderEntity::GetEntityEntries( std::deque<HpiEntry>& entries ) const
{
    SaErrorT rv;
    SaHpiEntityPathT child;
    // TODO update cnt
    SaHpiUint32T update_cnt;

    std::wstring path_str;

    SaHpiUint32T i = SAHPI_FIRST_ENTRY;
    while( i != SAHPI_LAST_ENTRY ) {
        SaHpiUint32T instance_id = i;

        rv = saHpiGetChildEntityPath( m_ctx.session_id, m_ctx.entity_path, &i, &child, &update_cnt );
        if( rv != SA_OK ) {
            break;
        }

        SaHpiEntityPathT child_short_ep;
        bool rc = SubstructHpiEntityPath( child, m_ctx.entity_path, child_short_ep );
        if ( !rc ) {
            break;
        }

        std::wstring name;
        MakeNameForEntity( child_short_ep, name );
        entries.push_back( HpiEntry( eHpiEntryEntity, instance_id, name ) );
    }
}

void cHpiSubProviderEntity::GetResourceEntries( std::deque<HpiEntry>& entries ) const
{
    SaErrorT rv;
    SaHpiResourceIdT rid;
    // TODO update cnt
    SaHpiUint32T update_cnt;
    SaHpiRptEntryT rpte;

    // Get Management Resources
    SaHpiUint32T i = SAHPI_FIRST_ENTRY;
    while( i != SAHPI_LAST_ENTRY ) {
        rv = saHpiGetIdByEntityPath( m_ctx.session_id,
                                     m_ctx.entity_path,
                                     SAHPI_NO_RECORD,
                                     &i,
                                     &rid,
                                     NULL,
                                     &update_cnt );
        if( rv != SA_OK ) {
            break;
        }

        rv = saHpiRptEntryGetByResourceId( m_ctx.session_id, rid, &rpte );
        if( rv != SA_OK ) {
            break;
        }

        std::wstring name;
        MakeNameForResource( rpte, name );
        entries.push_back( HpiEntry( eHpiEntryResource, rid, name ) );
    }
}

void cHpiSubProviderEntity::GetInstrumentEntries( SaHpiRdrTypeT type,
                                                  std::deque<HpiEntry>& entries ) const
{
    SaErrorT rv;
    // TODO update_cnt
    SaHpiUint32T update_cnt;
    SaHpiResourceIdT rid;
    SaHpiInstrumentIdT instr_id;
    SaHpiRdrT rdr;

    SaHpiUint32T i = SAHPI_FIRST_ENTRY;
    while( i != SAHPI_LAST_ENTRY ) {
        SaHpiUint32T instance_id = i;

        rv = saHpiGetIdByEntityPath( m_ctx.session_id,
                                     m_ctx.entity_path,
                                     type,
                                     &i,
                                     &rid,
                                     &instr_id,
                                     &update_cnt );
        if( rv != SA_OK ) {
            break;
        }

        rv = saHpiRdrGetByInstrumentId( m_ctx.session_id, rid, type, instr_id, &rdr );
        if( rv != SA_OK ) {
            break;
        }

        std::wstring name;
        MakeNameForInstrument( rdr, name );
        entries.push_back( HpiEntry( RdrType2EntryType( type ), instance_id, name ) );
    }
}

void cHpiSubProviderEntity::GetEntityEntryCtx( SaHpiUint32T instance_id, HpiEntryCtx& ctx ) const
{
    SaErrorT rv;
    SaHpiEntityPathT child;
    // TODO update_cnt
    SaHpiUint32T update_cnt;

    SaHpiUint32T i = instance_id;

    rv = saHpiGetChildEntityPath( m_ctx.session_id, m_ctx.entity_path, &i, &child, &update_cnt );
    if( rv != SA_OK ) {
        return;
    }

    ctx             = m_ctx;
    ctx.type        = eHpiEntryEntity;
    ctx.entity_path = child;
}

void cHpiSubProviderEntity::GetResourceEntryCtx( SaHpiResourceIdT rid, HpiEntryCtx& ctx ) const
{
    ctx             = m_ctx;
    ctx.type        = eHpiEntryResource;
    ctx.resource_id = rid;
}

void cHpiSubProviderEntity::GetInstrumentEntryCtx( SaHpiRdrTypeT type,
                                                   SaHpiUint32T instance_id,
                                                   HpiEntryCtx& ctx ) const
{
    SaErrorT rv;
    // TODO update_cnt
    SaHpiUint32T update_cnt;
    SaHpiResourceIdT rid;
    SaHpiInstrumentIdT instr_id;

    SaHpiUint32T i = instance_id;
    rv = saHpiGetIdByEntityPath( m_ctx.session_id,
                                 m_ctx.entity_path,
                                 type,
                                 &i,
                                 &rid,
                                 &instr_id,
                                 &update_cnt );
    if( rv != SA_OK ) {
        return;
    }

    ctx               = m_ctx;
    ctx.type          = RdrType2EntryType( type );
    ctx.resource_id   = rid;
    ctx.instrument_id = instr_id;
}

