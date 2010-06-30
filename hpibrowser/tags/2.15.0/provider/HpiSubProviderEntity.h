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


#ifndef __HPI_SUB_PROVIDER_ENTITY_H__
#define __HPI_SUB_PROVIDER_ENTITY_H__

#include <SaHpi.h>

#include <HpiSubProvider.h>


/************************************************
 * class cHpiSubProviderEntity
 ***********************************************/
class cHpiSubProviderEntity : public cHpiSubProvider
{
public:

    explicit cHpiSubProviderEntity();

    ~cHpiSubProviderEntity();


    void GetInfoHeader( std::wstring& txt ) const;

    void GetInfo( std::deque<HpiInfo>& info ) const;

    void GetActions( std::deque<HpiAction>& actions ) const;

    void ExecuteAction( const HpiActionShort& short_action );

    void GetEntries( std::deque<HpiEntry>& entries ) const;

    void GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const;

private:

    cHpiSubProviderEntity( const cHpiSubProviderEntity& );

    cHpiSubProviderEntity& operator =( const cHpiSubProviderEntity& );


    void GetEntityEntries( std::deque<HpiEntry>& entries ) const;

    void GetResourceEntries( std::deque<HpiEntry>& entries ) const;

    void GetInstrumentEntries( SaHpiRdrTypeT type, std::deque<HpiEntry>& entries ) const;

    void GetEntityEntryCtx( SaHpiUint32T instance_id, HpiEntryCtx& ctx ) const;

    void GetResourceEntryCtx( SaHpiResourceIdT rid, HpiEntryCtx& ctx ) const;

    void GetInstrumentEntryCtx( SaHpiRdrTypeT type,
                                SaHpiUint32T instance_id,
                                HpiEntryCtx& ctx ) const;
};


#endif // __HPI_SUB_PROVIDER_ENTITY_H__

