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


#ifndef __HPI_SUB_PROVIDER_H__
#define __HPI_SUB_PROVIDER_H__

#include <deque>
#include <string>

#include <HpiAction.h>
#include <HpiEntry.h>
#include <HpiInfo.h>


/************************************************
 * class cHpiSubProvider
 ***********************************************/
struct cHpiSubProvider
{
    explicit cHpiSubProvider( eHpiEntryType type )
        : m_type( type )
    {
        // empty
    }

    virtual ~cHpiSubProvider()
    {
        // empty
    }

    eHpiEntryType GetType() const
    {
        return m_type;
    }

    bool SetCtx( const HpiEntryCtx& ctx )
    {
        if ( ctx.type == m_type ) {
            m_ctx = ctx;
            return true;
        }
        return false;
    }

    virtual void GetInfoHeader( std::wstring& txt ) const = 0;

    virtual void GetInfo( std::deque<HpiInfo>& info ) const = 0;

    virtual void GetActions( std::deque<HpiAction>& actions ) const = 0;

    virtual void ExecuteAction( const HpiActionShort& short_action ) = 0;

    virtual void GetEntries( std::deque<HpiEntry>& enties ) const = 0;

    virtual void GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const = 0;

protected:


    // data
    eHpiEntryType m_type;
    HpiEntryCtx   m_ctx;
};


/************************************************
 * helpers for GetInfo
 ***********************************************/
template <class T1>
void Line( std::deque<HpiInfo>& info,
           const wchar_t * name,
           const T1& t1 )
{
    info.push_back( HpiInfo( name, t1 ) );
}

template <class T1, class T2>
void Line( std::deque<HpiInfo>& info,
           const wchar_t * name,
           const T1& t1,
           const T2& t2 )
{
    info.push_back( HpiInfo( name, t1, t2 ) );
}


#endif // __HPI_SUB_PROVIDER_H__

