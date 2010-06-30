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

#include "HpiSubProviderControl.h"


/************************************************
 * Control helpers
 ***********************************************/
static void GetSpecificInfo( SaHpiCtrlTypeT type,
                             const SaHpiCtrlRecUnionT& cru,
                             std::deque<HpiInfo>& info )
{
    Line( info, L"Control Specific Data", L"" );
    switch ( type ) {
        case SAHPI_CTRL_TYPE_DIGITAL:
            Line( info, L"  Default State", cru.Digital.Default );
            return;
        case SAHPI_CTRL_TYPE_DISCRETE:
            Line( info, L"  Default State", cru.Discrete.Default );
            return;
        case SAHPI_CTRL_TYPE_ANALOG:
            Line( info, L"  Min State", cru.Analog.Min, I32_SaHpiCtrlStateAnalog );
            Line( info, L"  Max State", cru.Analog.Max, I32_SaHpiCtrlStateAnalog );
            Line( info, L"  Default State", cru.Analog.Default, I32_SaHpiCtrlStateAnalog );
            return;
        case SAHPI_CTRL_TYPE_STREAM:
            Line( info, L"  Default Repeat", cru.Stream.Default.Repeat, UI8_SaHpiBool );
            Line( info,
                  L"  Default Stream",
                  &cru.Stream.Default.Stream[0],
                  cru.Stream.Default.StreamLength );
            return;
        case SAHPI_CTRL_TYPE_TEXT:
            Line( info, L"  Max Chars Per Line", cru.Text.MaxChars );
            Line( info, L"  Max Lines", cru.Text.MaxLines );
            Line( info, L"  Language", cru.Text.Language );
            Line( info, L"  Data Type", cru.Text.DataType );
            {
                std::wstring name;
                std::wstring line;
                ToTxt( cru.Text.Default.Line, line, UI8_SaHpiTxtLineNum );
                name = L"  Default Line ";
                name += line;
                Line( info, name.c_str(), cru.Text.Default.Text );
            }
            return;
        case SAHPI_CTRL_TYPE_OEM:
            Line( info, L"  Manufacturer Id", cru.Oem.MId );
            Line( info,
                  L"  Config Data",
                  cru.Oem.ConfigData,
                  SAHPI_CTRL_OEM_CONFIG_LENGTH );
            Line( info, L"  Default Manufacturer Id", cru.Oem.Default.MId );
            Line( info,
                  L"  Default Body",
                  cru.Oem.Default.Body,
                  cru.Oem.Default.BodyLength );
            return;
        default:
            break;
    }
}

static void GetStateInfo( const SaHpiCtrlStateT& state, std::deque<HpiInfo>& info )
{
    const SaHpiCtrlStateUnionT& su = state.StateUnion;

    switch ( state.Type ) {
        case SAHPI_CTRL_TYPE_DIGITAL:
            Line( info, L"Current State", su.Digital );
            return;
        case SAHPI_CTRL_TYPE_DISCRETE:
            Line( info, L"Current State", su.Discrete, UI32_SaHpiCtrlStateDiscrete );
            return;
        case SAHPI_CTRL_TYPE_ANALOG:
            Line( info, L"Current State", su.Analog, I32_SaHpiCtrlStateAnalog );
            return;
        case SAHPI_CTRL_TYPE_STREAM:
            Line( info, L"Current Repeat", su.Stream.Repeat, UI8_SaHpiBool );
            Line( info,
                  L"Current Stream",
                  &su.Stream.Stream[0],
                  su.Stream.StreamLength );
            return;
        case SAHPI_CTRL_TYPE_TEXT:
            {
                std::wstring name;
                std::wstring line;
                ToTxt( su.Text.Line, line, UI8_SaHpiTxtLineNum );
                name = L"Current Line ";
                name += line;
                Line( info, name.c_str(), su.Text.Text );
            }
            return;
        case SAHPI_CTRL_TYPE_OEM:
            Line( info, L"Current Manufacturer Id", su.Oem.MId );
            Line( info,
                  L"Current Body",
                  su.Oem.Body,
                  su.Oem.BodyLength );
            return;
        default:
            break;
    }
}


/************************************************
 * class cHpiSubProviderControl
 ***********************************************/
cHpiSubProviderControl::cHpiSubProviderControl()
    : cHpiSubProvider( eHpiEntryControl )
{
    // empty
}

cHpiSubProviderControl::~cHpiSubProviderControl()
{
    // empty
}

void cHpiSubProviderControl::GetInfoHeader( std::wstring& txt ) const
{
    MakeShortNameForInstrument( SAHPI_CTRL_RDR, m_ctx.instrument_id, txt );
}

void cHpiSubProviderControl::GetInfo( std::deque<HpiInfo>& info ) const
{
    info.clear();

    SaErrorT rv;

    SaHpiRdrT rdr;
    rv = saHpiRdrGetByInstrumentId( m_ctx.session_id,
                                    m_ctx.resource_id,
                                    SAHPI_CTRL_RDR,
                                    m_ctx.instrument_id,
                                    &rdr );
    if ( rv != SA_OK ) {
        Line( info, L"saHpiRdrGetByInstrumentId failed", rv, I32_SaError );
        return;
    }

    Line( info, L"Resource Id", m_ctx.resource_id, UI32_SaHpiResourceId );
    Line( info, L"Entity", rdr.Entity );
    Line( info, L"IsFru", rdr.IsFru, UI8_SaHpiBool );

    const SaHpiCtrlRecT& cr = rdr.RdrTypeUnion.CtrlRec;

    Line( info, L"Control Num", cr.Num, UI32_SaHpiCtrlNum );
    Line( info, L"Output Type", cr.OutputType );
    Line( info, L"Type", cr.Type );
    GetSpecificInfo( cr.Type, cr.TypeUnion, info );
    Line( info, L"Default Mode", cr.DefaultMode.Mode );
    Line( info, L"Mode Read Only", cr.DefaultMode.ReadOnly, UI8_SaHpiBool );
    Line( info, L"Write Only", cr.WriteOnly, UI8_SaHpiBool );
    Line( info, L"OEM", cr.Oem );
    Line( info, L"IdString", rdr.IdString );

    if( cr.WriteOnly == SAHPI_FALSE ) {
        SaHpiUint32T n = ( cr.Type == SAHPI_CTRL_TYPE_TEXT ) ? cr.TypeUnion.Text.MaxLines : 1;
        for ( SaHpiUint32T i = 1; i <= n; ++i ) {
            SaHpiCtrlModeT mode;
            SaHpiCtrlStateT state;

            state.StateUnion.Text.Line = i;
            rv = saHpiControlGet( m_ctx.session_id,
                                  m_ctx.resource_id,
                                  m_ctx.instrument_id,
                                  &mode,
                                  &state );
            if ( rv != SA_OK ) {
                Line( info, L"saHpiControlGet failed", rv, I32_SaError );
                return;
            }
            if ( i == 1 ) {
                Line( info, L"Current Mode", mode );
            }

            GetStateInfo( state, info );
        }
    }
}

void cHpiSubProviderControl::GetActions( std::deque<HpiAction>& actions ) const
{
    actions.clear();
    actions.push_back( HpiAction( 1, L"TODO" ) );
}

void cHpiSubProviderControl::ExecuteAction( const HpiActionShort& )
{
//    printf( "Execute Action %d\n", short_action.id );
}

void cHpiSubProviderControl::GetEntries( std::deque<HpiEntry>& entries ) const
{
    entries.clear();
}

void cHpiSubProviderControl::GetEntryCtx( const HpiEntryShort&, HpiEntryCtx& ctx ) const
{
    ctx.type = eHpiEntryUnknown;
}

