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
#include "HpiSubProviderFUMIBank.h"


/************************************************
 * class cHpiSubProviderFUMIBank
 ***********************************************/
cHpiSubProviderFUMIBank::cHpiSubProviderFUMIBank()
    : cHpiSubProvider( eHpiEntryFUMIBank )
{
    // empty
}

cHpiSubProviderFUMIBank::~cHpiSubProviderFUMIBank()
{
    // empty
}

void cHpiSubProviderFUMIBank::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForFUMIBank( m_ctx.bank_num, txt );
}

void cHpiSubProviderFUMIBank::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    Line( info, L"FUMI Num", m_ctx.instrument_id, UI32_SaHpiFumiNum );
    GetBankInfo( info );
    GetLogicalBankInfo( info );
    GetUpgradeStatusInfo( info );
    GetAutoRollbackDisableInfo( info );
}

void cHpiSubProviderFUMIBank::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderFUMIBank::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderFUMIBank::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();

    GetSourceEntry( entries );
    GetComponentEntries( entries );
}

void cHpiSubProviderFUMIBank::GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const
{
    if ( short_entry.type == eHpiEntryFUMISource ) {
        ctx      = m_ctx;
        ctx.type = eHpiEntryFUMISource;
    } else if ( short_entry.type == eHpiEntryFUMIComponent ) {
        ctx              = m_ctx;
        ctx.type         = eHpiEntryFUMIComponent;
        ctx.component_id = short_entry.id;
    } else {
        ctx.type = eHpiEntryUnknown;
        return;
    }
}

void cHpiSubProviderFUMIBank::GetBankInfo( std::deque<HpiInfo>& info ) const
{
    SaErrorT rv;
    SaHpiFumiBankInfoT bi;

    rv = saHpiFumiTargetInfoGet( m_ctx.session_id,
                                 m_ctx.resource_id,
                                 m_ctx.instrument_id,
                                 m_ctx.bank_num,
                                 &bi );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiFumiTargetInfoGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Bank Id", bi.BankId );
    Line( info, L"Size, kB", bi.BankSize );
    Line( info, L"Position in Boot Order", bi.Position );
    Line( info, L"State", bi.BankState );

    SaHpiFumiFirmwareInstanceInfoT main_fwii;
    MakeMainFwInstanceInfo( bi, main_fwii );
    GetFwInstanceInfo( L"Main Firmware Instance", main_fwii, info );
}

void cHpiSubProviderFUMIBank::GetLogicalBankInfo( std::deque<HpiInfo>& info ) const
{
    if ( m_ctx.bank_num != SAHPI_LOGICAL_BANK_NUM ) {
        return;
    }

    SaErrorT rv;
    SaHpiFumiLogicalBankInfoT lbi;
    rv = saHpiFumiLogicalTargetInfoGet( m_ctx.session_id,
                                        m_ctx.resource_id,
                                        m_ctx.instrument_id,
                                        &lbi );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiFumiLogicalTargetInfoGet failed", rv, I32_SaError );
        return;
    }

    Line( info,
          L"Firmware Persistent Location Count",
          lbi.FirmwarePersistentLocationCount );
    Line( info,
          L"Logical Bank State Flags",
          lbi.BankStateFlags,
          UI32_SaHpiFumiLogicalBankStateFlags );
    GetFwInstanceInfo( L"Pending Firmware Instance", lbi.PendingFwInstance, info );
    GetFwInstanceInfo( L"Rollback Firmware Instance", lbi.RollbackFwInstance, info );
}

void cHpiSubProviderFUMIBank::GetUpgradeStatusInfo( std::deque<HpiInfo>& info ) const
{
    SaErrorT rv;
    SaHpiFumiUpgradeStatusT status;
    rv = saHpiFumiUpgradeStatusGet( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    m_ctx.instrument_id,
                                    m_ctx.bank_num,
                                    &status );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiFumiUpgradeStatusGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Upgrade Status", status );
}

void cHpiSubProviderFUMIBank::GetAutoRollbackDisableInfo( std::deque<HpiInfo>& info ) const
{
    if ( m_ctx.bank_num != SAHPI_LOGICAL_BANK_NUM ) {
        return;
    }

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
    if ( ( caps & SAHPI_FUMI_CAP_AUTOROLLBACK ) == 0 ) {
        return;
    }

    SaHpiBoolT disabled;
    rv = saHpiFumiAutoRollbackDisableGet( m_ctx.session_id,
                                          m_ctx.resource_id,
                                          m_ctx.instrument_id,
                                          &disabled );
    if ( rv != SA_OK ) {
        return;
    }

    Line( info, L"Auto Rollback Disabled", disabled, UI8_SaHpiBool );
}

void cHpiSubProviderFUMIBank::GetSourceEntry( std::deque<HpiEntry>& entries ) const
{
    SaErrorT rv;
    SaHpiFumiSourceInfoT si;

    rv = saHpiFumiSourceInfoGet( m_ctx.session_id,
                                 m_ctx.resource_id,
                                 m_ctx.instrument_id,
                                 m_ctx.bank_num,
                                 &si );
    if ( rv == SA_ERR_HPI_INVALID_REQUEST ) {
        return;
    }
    if ( rv != SA_OK ) {
        return;
    }

    std::wstring name;
    MakeNameForFUMISource( si, name );
    entries.push_back( HpiEntry( eHpiEntryFUMISource, 0, name ) );
}

void cHpiSubProviderFUMIBank::GetComponentEntries( std::deque<HpiEntry>& entries ) const
{
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
        rv = saHpiFumiTargetComponentInfoGet( m_ctx.session_id,
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
        MakeNameForFUMIComponent( ci, name );
        entries.push_back( HpiEntry( eHpiEntryFUMIComponent, ci.ComponentId, name ) );

        first = false;
        id = next_id;
    }
}

