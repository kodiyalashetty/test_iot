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


#ifndef __HPI_SUB_PROVIDER_FUMI_COMPONENT_H__
#define __HPI_SUB_PROVIDER_FUMI_COMPONENT_H__

#include <SaHpi.h>

#include <HpiSubProvider.h>


/************************************************
 * class cHpiSubProviderFUMIComponent
 ***********************************************/
class cHpiSubProviderFUMIComponent : public cHpiSubProvider
{
public:

    explicit cHpiSubProviderFUMIComponent();

    ~cHpiSubProviderFUMIComponent();


    bool SetCtx( const HpiEntryCtx& ctx );

    void GetInfoHeader( std::wstring& txt ) const;

    void GetInfo( std::deque<HpiInfo>& info ) const;

    void GetActions( std::deque<HpiAction>& actions ) const;

    void ExecuteAction( const HpiActionShort& short_action );

    void GetEntries( std::deque<HpiEntry>& entries ) const;

    void GetEntryCtx( const HpiEntryShort& short_entry, HpiEntryCtx& ctx ) const;

private:

    cHpiSubProviderFUMIComponent( const cHpiSubProviderFUMIComponent& );

    cHpiSubProviderFUMIComponent& operator =( const cHpiSubProviderFUMIComponent& );


    void GetComponentInfo( std::deque<HpiInfo>& info ) const;

    void GetLogicalComponentInfo( std::deque<HpiInfo>& info ) const;
};


#endif // __HPI_SUB_PROVIDER_FUMI_COMPONENT_H__
