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


#ifndef __HPI_PROVIDER_H__
#define __HPI_PROVIDER_H__

#include <deque>
#include <string>
#include <utility>

#include <SaHpi.h>

#include <HpiAction.h>
#include <HpiEntry.h>
#include <HpiInfo.h>
#include <View.h>


/************************************************
 * class cHpiProvider
 ***********************************************/
struct cHpiProvider
{
    explicit cHpiProvider()
        : m_view( 0 )
    {
        // empty
    }

    void SetView( cView * view )
    {
        m_view = view;
    }

    virtual void GetInfoHeader( std::wstring& txt ) const = 0;

    virtual void GetInfo( std::deque<HpiInfo>& info ) const = 0;

    virtual void GetActions( std::deque<HpiAction>& actions ) const = 0;

    virtual void ExecuteAction( const HpiActionShort& short_action ) = 0;

    virtual void GetEntries( std::deque<HpiEntry>& entries ) = 0;

    virtual void Enter( const HpiEntryShort& short_entry ) = 0;

protected:

    virtual ~cHpiProvider()
    {
        // empty
    }

    void UpdateView()
    {
        if ( m_view ) {
            m_view->Update();
        }
    }

private:

    cHpiProvider( const cHpiProvider& );

    cHpiProvider& operator =( const cHpiProvider& );


    // data
    cView * m_view;
};


#endif // __HPI_PROVIDER_H__

