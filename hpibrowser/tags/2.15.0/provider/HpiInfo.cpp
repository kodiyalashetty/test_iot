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


#include <HpiInfo.h>
#include <HpiUtils.h>


/************************************************
 * class HpiInfo
 ***********************************************/
HpiInfo::HpiInfo( const wchar_t * _name, const wchar_t * txt )
    : name( _name ), value( txt )
{
    // empty
}

HpiInfo::HpiInfo( const wchar_t * _name, const wchar_t * txt, unsigned int size )
    : name( _name )
{
    if ( txt ) {
        value.assign( txt, txt + size );
    }
}

HpiInfo::HpiInfo( const wchar_t * _name, const std::wstring& _value )
    : name( _name ), value( _value )
{
    // empty
}

HpiInfo::HpiInfo( const wchar_t * _name, wchar_t * txt )
    : name( _name ), value( txt )
{
    // empty
}

HpiInfo::HpiInfo( const wchar_t * _name, wchar_t * txt, unsigned int size )
    : name( _name )
{
    if ( txt ) {
        value.assign( txt, txt + size );
    }
}

HpiInfo::HpiInfo( const wchar_t * _name, std::wstring& _value )
    : name( _name ), value( _value )
{
    // empty
}


HpiInfo::HpiInfo( const wchar_t * _name, SaHpiUint8T ui8, UI8_Fmt fmt )
    : name( _name )
{
    ToTxt( ui8, value, fmt );
}


HpiInfo::HpiInfo( const wchar_t * _name, SaHpiUint16T ui16, UI16_Fmt fmt )
    : name( _name )
{
    ToTxt( ui16, value, fmt );
}

HpiInfo::HpiInfo( const wchar_t * _name, SaHpiInt32T i32, I32_Fmt fmt )
    : name( _name )
{
    ToTxt( i32, value, fmt );
}

HpiInfo::HpiInfo( const wchar_t * _name, SaHpiUint32T ui32, UI32_Fmt fmt )
    : name( _name )
{
    ToTxt( ui32, value, fmt );
}

HpiInfo::HpiInfo( const wchar_t * _name, const SaHpiInt64T& i64, I64_Fmt fmt )
    : name( _name )
{
    ToTxt( i64, value, fmt );
}

HpiInfo::HpiInfo( const wchar_t * _name, SaHpiFloat64T f64, F64_Fmt fmt )
    : name( _name )
{
    ToTxt( f64, value, fmt );
}

HpiInfo::HpiInfo( const wchar_t * _name, const SaHpiUint8T * binary, SaHpiUint16T len )
    : name( _name )
{
    ToTxt( binary, len, value );
}

