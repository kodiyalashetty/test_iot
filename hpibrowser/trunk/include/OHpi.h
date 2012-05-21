/*
 *  Copyright (c) 2012 Pigeon Point Systems.
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
 */


#ifndef __OHPI_H__
#define __OHPI_H__

#include <SaHpi.h>

#include <HpiProvider.h>


/************************************************
 * class cOHpi
 ***********************************************/
class cOHpi : public cHpiProvider
{
public:

    explicit cOHpi();

    ~cOHpi();

    void GetInfoHeader( std::wstring& txt ) const;

    void GetInfo( std::deque<HpiInfo>& info ) const;

    void GetActions( std::deque<HpiAction>& actions ) const;

    void ExecuteAction( const HpiActionShort& short_action );

    void GetEntries( std::deque<HpiEntry>& entries );

    void Enter( const HpiEntryShort& short_entry );

    bool IsDidSelected() const
    {
        return m_selected;
    }

    SaHpiDomainIdT GetSelectedDid() const
    {
        return m_selected_did;
    }

    void EnterNew( const std::string& host_port );

private:

    cOHpi( const cOHpi& );
    cOHpi& operator =( const cOHpi& );

private: // data

    bool           m_selected;
    SaHpiDomainIdT m_selected_did;
};


#endif // __OHPI_H__

