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


#ifndef __HPI_H__
#define __HPI_H__

#include <stack>
#include <tr1/unordered_map>

#include <SaHpi.h>

#include <HpiProvider.h>
#include <HpiSubProvider.h>


/************************************************
 * class cHpi
 ***********************************************/
class cHpi : public cHpiProvider
{
public:

    explicit cHpi( SaHpiDomainIdT startup_did );

    ~cHpi();


    void GetInfoHeader( std::wstring& txt ) const;

    void GetInfo( std::deque<HpiInfo>& info ) const;

    void GetActions( std::deque<HpiAction>& actions ) const;

    void ExecuteAction( const HpiActionShort& short_action );

    void GetEntries( std::deque<HpiEntry>& entries );

    void Enter( const HpiEntryShort& short_entry );

private:

    cHpi( const cHpi& );

    cHpi& operator =( const cHpi& );

    cHpiSubProvider * GetSP() const;

    bool GetSessionForDomain( SaHpiDomainIdT did, SaHpiSessionIdT& sid );


    // data
    typedef std::tr1::unordered_map<SaHpiDomainIdT, SaHpiSessionIdT> Sessions;
    Sessions m_sessions;

    HpiEntryCtx             m_ctx;
    std::stack<HpiEntryCtx> m_ctx_stack;

    cHpiSubProvider *             m_unknown_sp;
    std::deque<cHpiSubProvider *> m_known_sps;
    cHpiSubProvider *             m_sp_map[NumberOfHpiEntryTypes];
};


#endif // __HPI_H__

