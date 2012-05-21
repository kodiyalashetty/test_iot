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


#include <Hpi.h>
#include "HpiSubProviderAlarm.h"
#include "HpiSubProviderAnnouncement.h"
#include "HpiSubProviderAnnunciator.h"
#include "HpiSubProviderControl.h"
#include "HpiSubProviderDAT.h"
#include "HpiSubProviderDET.h"
#include "HpiSubProviderDIMI.h"
#include "HpiSubProviderDIMITest.h"
#include "HpiSubProviderDomain.h"
#include "HpiSubProviderDRT.h"
#include "HpiSubProviderEntity.h"
#include "HpiSubProviderFUMI.h"
#include "HpiSubProviderFUMIBank.h"
#include "HpiSubProviderFUMIComponent.h"
#include "HpiSubProviderFUMISource.h"
#include "HpiSubProviderFUMISourceComponent.h"
#include "HpiSubProviderHotSwap.h"
#include "HpiSubProviderIdr.h"
#include "HpiSubProviderIdrArea.h"
#include "HpiSubProviderIdrField.h"
#include "HpiSubProviderLogEntry.h"
#include "HpiSubProviderLog.h"
#include "HpiSubProviderPower.h"
#include "HpiSubProviderResource.h"
#include "HpiSubProviderReset.h"
#include "HpiSubProviderRPT.h"
#include "HpiSubProviderSensor.h"
#include "HpiSubProviderUnknown.h"
#include "HpiSubProviderWatchdog.h"


/************************************************
 * class cHpi
 ***********************************************/
cHpi::cHpi( SaHpiDomainIdT startup_did )
{
    m_unknown_sp = new cHpiSubProviderUnknown;


    m_known_sps.push_back( new cHpiSubProviderDomain );
    m_known_sps.push_back( new cHpiSubProviderDRT );
    m_known_sps.push_back( new cHpiSubProviderRPT );
    m_known_sps.push_back( new cHpiSubProviderDET );
    m_known_sps.push_back( new cHpiSubProviderLog );
    m_known_sps.push_back( new cHpiSubProviderDAT );
    m_known_sps.push_back( new cHpiSubProviderResource );
    m_known_sps.push_back( new cHpiSubProviderAlarm );
    m_known_sps.push_back( new cHpiSubProviderLogEntry );
    m_known_sps.push_back( new cHpiSubProviderEntity );
    m_known_sps.push_back( new cHpiSubProviderControl );
    m_known_sps.push_back( new cHpiSubProviderSensor );
    m_known_sps.push_back( new cHpiSubProviderIdr );
    m_known_sps.push_back( new cHpiSubProviderWatchdog );
    m_known_sps.push_back( new cHpiSubProviderAnnunciator );
    m_known_sps.push_back( new cHpiSubProviderDIMI );
    m_known_sps.push_back( new cHpiSubProviderFUMI );
    m_known_sps.push_back( new cHpiSubProviderReset );
    m_known_sps.push_back( new cHpiSubProviderPower );
    m_known_sps.push_back( new cHpiSubProviderHotSwap );
    m_known_sps.push_back( new cHpiSubProviderIdrArea );
    m_known_sps.push_back( new cHpiSubProviderAnnouncement );
    m_known_sps.push_back( new cHpiSubProviderDIMITest );
    m_known_sps.push_back( new cHpiSubProviderFUMIBank );
    m_known_sps.push_back( new cHpiSubProviderIdrField );
    m_known_sps.push_back( new cHpiSubProviderFUMIComponent );
    m_known_sps.push_back( new cHpiSubProviderFUMISource );
    m_known_sps.push_back( new cHpiSubProviderFUMISourceComponent );

    for ( unsigned int i = 0; i < NumberOfHpiEntryTypes; ++i ) {
        m_sp_map[i] = m_unknown_sp;
    }
    for ( unsigned int i = 0, n = m_known_sps.size(); i < n; ++i ) {
        m_sp_map[ m_known_sps[i]->GetType() ] = m_known_sps[i];
    }

    // TODO redo with Enter
    // TODO move from CTOR
    // Root context
    m_ctx.type = eHpiEntryDomain;
    m_ctx.domain_id = startup_did;
    // TODO
    bool rc = GetSessionForDomain( m_ctx.domain_id, m_ctx.session_id );
    if ( !rc ) {
        // TODO
    }

    GetSP()->SetCtx( m_ctx );
}

cHpi::~cHpi()
{
    // Ignore possible error on saHpiSessionClose;
    Sessions::const_iterator iter = m_sessions.begin();
    Sessions::const_iterator end  = m_sessions.end();
    for ( ; iter != end; ++iter ) {
        saHpiSessionClose( iter->second );
    }

    for ( unsigned int i = 0, n = m_known_sps.size(); i < n; ++i ) {
        delete m_known_sps[i];
    }

    delete m_unknown_sp;
}

void cHpi::GetInfoHeader( std::wstring& txt ) const
{
    GetSP()->GetInfoHeader( txt );
}

void cHpi::GetInfo( std::deque<HpiInfo>& info ) const
{
    GetSP()->GetInfo( info );
}

void cHpi::GetActions( std::deque<HpiAction>& actions ) const
{
    GetSP()->GetActions( actions );
}

void cHpi::ExecuteAction( const HpiActionShort& short_action )
{
    GetSP()->ExecuteAction( short_action );
}

void cHpi::GetEntries( std::deque<HpiEntry>& entries )
{
    GetSP()->GetEntries( entries );
    if ( !m_ctx_stack.empty() ) {
        std::wstring upname;
        MakeNameForUp( upname );
        entries.push_front( HpiEntry( eHpiEntryUp, 0, upname ) );
    }
}

void cHpi::Enter( const HpiEntryShort& short_entry )
{
    if ( short_entry.type == eHpiEntryUp ) {
        if ( !m_ctx_stack.empty() ) {
            m_ctx = m_ctx_stack.top();
            m_ctx_stack.pop();
        }
    } else {
        HpiEntryCtx new_ctx;
        GetSP()->GetEntryCtx( short_entry, new_ctx );
        m_ctx_stack.push( m_ctx );
        m_ctx = new_ctx;
    }

    GetSP()->SetCtx( m_ctx );
    UpdateView();
}

cHpiSubProvider * cHpi::GetSP() const
{
    if ( ( m_ctx.type < eHpiEntryUnknown ) || ( m_ctx.type >= NumberOfHpiEntryTypes ) ) {
        return m_unknown_sp;
    } else {
        return m_sp_map[ m_ctx.type ];
    }
}

bool cHpi::GetSessionForDomain( SaHpiDomainIdT did, SaHpiSessionIdT& sid )
{
    Sessions::const_iterator iter = m_sessions.find( did );
    if ( iter != m_sessions.end() ) {
        sid = iter->second;
    } else {
        SaErrorT rv = saHpiSessionOpen( did, &sid, 0 );
        if ( rv != SA_OK ) {
            return false;
        }
        m_sessions[did] = sid;
    }
    return true;
}

