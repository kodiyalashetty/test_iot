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

#include "HpiSubProviderFUMI.h"


/************************************************
 * FUMI helpers
 ***********************************************/
static void GetSpecInfo( const SaHpiFumiSpecInfoT& si,
                         std::deque<HpiInfo>& info )
{
    Line( info, L"Underlying Specification Framework", L"" );

    const SaHpiFumiSpecInfoTypeUnionT& siu = si.SpecInfoTypeUnion;
    switch ( si.SpecInfoType ) {
        case SAHPI_FUMI_SPEC_INFO_SAF_DEFINED:
            Line( info, L"  Specification Id", siu.SafDefined.SpecID );
            Line( info, L"  Specification Revision", siu.SafDefined.RevisionID );
            return;
        case SAHPI_FUMI_SPEC_INFO_OEM_DEFINED:
            Line( info, L"  Manufacturer Id", siu.OemDefined.Mid );
            Line( info,
                  L"  Body",
                  siu.OemDefined.Body,
                  siu.OemDefined.BodyLength );
            return;
        default:
            break;
    }

}

/************************************************
 * class cHpiSubProviderFUMI
 ***********************************************/
cHpiSubProviderFUMI::cHpiSubProviderFUMI()
    : cHpiSubProvider( eHpiEntryFUMI )
{
    // empty
}

cHpiSubProviderFUMI::~cHpiSubProviderFUMI()
{
    // empty
}

void cHpiSubProviderFUMI::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForInstrument( SAHPI_FUMI_RDR, m_ctx.instrument_id, txt );
}

void cHpiSubProviderFUMI::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;

    SaHpiRdrT rdr;
    rv = saHpiRdrGetByInstrumentId( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    SAHPI_FUMI_RDR,
                                    m_ctx.instrument_id,
                                    &rdr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiRdrGetByInstrumentId failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );
    Line( info, L"Entity", rdr.Entity );
    Line( info, L"IsFru", rdr.IsFru, UI8_SaHpiBool );

    const SaHpiFumiRecT& fr = rdr.RdrTypeUnion.FumiRec;

    Line( info, L"FUMI Num", fr.Num, UI32_SaHpiFumiNum );
    Line( info, L"Access Protocols", fr.AccessProt, UI32_SaHpiFumiProtocol );
    Line( info, L"Capabilities", fr.Capability, UI32_SaHpiFumiCapability );
    Line( info, L"Number of Explicit Banks", fr.NumBanks );
    Line( info, L"OEM", fr.Oem );
    Line( info, L"IdString", rdr.IdString );

    SaHpiFumiSpecInfoT spec_info;
    rv = saHpiFumiSpecInfoGet( m_ctx.session_id,
                               m_ctx.resource_id,
                               m_ctx.instrument_id,
                               &spec_info );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiFumiSpecInfoGet failed", rv, I32_SaError );
        return;
    }
    GetSpecInfo( spec_info, info );

    SaHpiFumiServiceImpactDataT service_impact;
    rv = saHpiFumiServiceImpactGet( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    m_ctx.instrument_id,
                                    &service_impact );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiFumiServiceImpactGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"Service Impact", L"" );
    for ( SaHpiUint32T i = 0; i < service_impact.NumEntities; ++i ) {
        // TODO revisit
        Line( info, L"  Entity", service_impact.ImpactedEntities[i].ImpactedEntity );
        Line( info, L"    Impact", service_impact.ImpactedEntities[i].ServiceImpact );
    }
}

void cHpiSubProviderFUMI::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderFUMI::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderFUMI::GetEntries( std::deque<HpiEntry>& entries ) const
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

    std::wstring lbname;
    MakeNameForFUMIBank( SAHPI_LOGICAL_BANK_NUM, lbname );
    entries.push_back( HpiEntry( eHpiEntryFUMIBank, SAHPI_LOGICAL_BANK_NUM, lbname ) );

    for ( SaHpiUint32T bnum = 1; bnum <= rdr.RdrTypeUnion.FumiRec.NumBanks; ++bnum ) {
        std::wstring bname;
        MakeNameForFUMIBank( bnum, bname );
        entries.push_back( HpiEntry( eHpiEntryFUMIBank, bnum, bname ) );
    }
}

void cHpiSubProviderFUMI::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;

    if( short_entry.type != eHpiEntryFUMIBank ) {
        return;
    }

    ctx          = m_ctx;
    ctx.type     = eHpiEntryFUMIBank;
    ctx.bank_num = short_entry.id;
}

