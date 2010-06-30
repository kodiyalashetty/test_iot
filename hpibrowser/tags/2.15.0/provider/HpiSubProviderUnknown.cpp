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


#include "HpiSubProviderUnknown.h"


/************************************************
 * class cHpiSubProviderUnknown
 ***********************************************/
cHpiSubProviderUnknown::cHpiSubProviderUnknown()
    : cHpiSubProvider( eHpiEntryUnknown )
{
    // empty
}

cHpiSubProviderUnknown::~cHpiSubProviderUnknown()
{
    // empty
}

void cHpiSubProviderUnknown::GetInfoHeader( std::wstring& txt ) const
{
    MakeNameForUnknown( txt );
}

void cHpiSubProviderUnknown::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();
    Line( info, L"Unimplemented Subprovider", L"TODO" );
}

void cHpiSubProviderUnknown::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    // Here shall be Unknown actions
}

void cHpiSubProviderUnknown::ExecuteAction( const HpiActionShort& )
{
    // Here shall be Unknown action execution
}

void cHpiSubProviderUnknown::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
    // Here shall be Unknown entries
}

void cHpiSubProviderUnknown::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx      = m_ctx;
    ctx.type = eHpiEntryUnknown;
}

