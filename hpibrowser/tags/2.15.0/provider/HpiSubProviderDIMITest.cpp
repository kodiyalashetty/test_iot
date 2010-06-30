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

#include "HpiSubProviderDIMITest.h"


/************************************************
 * class cHpiSubProviderDIMITest
 ***********************************************/
cHpiSubProviderDIMITest::cHpiSubProviderDIMITest()
    : cHpiSubProvider( eHpiEntryDIMITest )
{
    // empty
}

cHpiSubProviderDIMITest::~cHpiSubProviderDIMITest()
{
    // empty
}

void cHpiSubProviderDIMITest::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForDIMITest( m_ctx.test_num, txt );
}

void cHpiSubProviderDIMITest::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;

    SaHpiDimiTestT dti;
    rv = saHpiDimiTestInfoGet( m_ctx.session_id,
                               m_ctx.resource_id,
                               m_ctx.instrument_id,
                               m_ctx.test_num,
                               &dti );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiDimiTestInfoGet failed", rv, I32_SaError );
        return;
    }

    Line( info, L"DIMI Num", m_ctx.instrument_id, UI32_SaHpiDimiNum );
    Line( info, L"Test Num", m_ctx.test_num, UI32_SaHpiDimiTestNum );
    Line( info, L"Service Impact", dti.ServiceImpact );
    for ( SaHpiUint32T i = 0; i < SAHPI_DIMITEST_MAX_ENTITIESIMPACTED; ++i ) {
        // TODO revisit
        std::wstring entity_num;
        ToTxt( i, entity_num, UI32_Dec );
        std::wstring entity_name = L"  Entity ";
        entity_name += entity_num;
        Line( info, entity_name.c_str(), dti.EntitiesImpacted[i].EntityImpacted );

        Line( info, L"    Impact", dti.EntitiesImpacted[i].ServiceImpact );
    }
    if ( dti.NeedServiceOS != SAHPI_FALSE ) {
        Line( info, L"Needed Service OS", dti.ServiceOS );
    }
    // TOD investigate - TimeT or TimeoutT?
    Line( info, L"Expected Run Duration", dti.ExpectedRunDuration, I64_SaHpiTime );
    Line( info, L"Capabilities", dti.TestCapabilities, UI32_SaHpiDimiTestCapability );
    // TODO parse SaHpiDimiTestParamsDefinitionT
    Line( info, L"Parameters Definition", L"TODO" );

    SaHpiDimiReadyT dr;
    rv = saHpiDimiTestReadinessGet( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    m_ctx.instrument_id,
                                    m_ctx.test_num,
                                    &dr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiDimiTestReadinessGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"Current Test Readiness", dr );

    SaHpiDimiTestPercentCompletedT pc;
    SaHpiDimiTestRunStatusT rs;
    rv = saHpiDimiTestStatusGet( m_ctx.session_id,
                                 m_ctx.resource_id,
                                 m_ctx.instrument_id,
                                 m_ctx.test_num,
                                 &pc,
                                 &rs );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiDimiTestStatusGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"Current Test Run Status", rs );
    if ( rs == SAHPI_DIMITEST_STATUS_RUNNING ) {
        Line( info,
              L"Current Percentage of Test Completed",
              pc,
              UI8_SaHpiDimiTestPercentCompleted );
    }

    SaHpiDimiTestResultsT tr;
    rv = saHpiDimiTestResultsGet( m_ctx.session_id,
                                  m_ctx.resource_id,
                                  m_ctx.instrument_id,
                                  m_ctx.test_num,
                                  &tr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiDimiTestResultsGet failed", rv, I32_SaError );
        return;
    }
    Line( info, L"Last Run Results", L"" );
    Line( info, L"  Results Timestamp", tr.ResultTimeStamp, I64_SaHpiTime );
    Line( info, L"  Run Duration, ns", tr.RunDuration, I64_SaHpiTimeout );
    Line( info, L"  Test Run Status", tr.LastRunStatus );
    Line( info, L"  Error Code", tr.TestErrorCode );
    Line( info, L"  Results String", tr.TestResultString );
    Line( info, L"  Results String Is URL", tr.TestResultStringIsURI, UI8_SaHpiBool );
}

void cHpiSubProviderDIMITest::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderDIMITest::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderDIMITest::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderDIMITest::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

