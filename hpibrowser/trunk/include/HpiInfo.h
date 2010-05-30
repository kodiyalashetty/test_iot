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


#ifndef __HPI_INFO_H__
#define __HPI_INFO_H__

#include <string>

#include <SaHpi.h>

#include <HpiUtils.h>


/************************************************
 * class HpiInfo
 ***********************************************/
struct HpiInfo
{
    explicit HpiInfo( const wchar_t * _name, const wchar_t * txt );

    explicit HpiInfo( const wchar_t * _name, const wchar_t * txt, unsigned int size );

    explicit HpiInfo( const wchar_t * _name, const std::wstring& _value );


    // TODO get rid on non-const wchar_t CTORs
    explicit HpiInfo( const wchar_t * _name, wchar_t * txt );

    explicit HpiInfo( const wchar_t * _name, wchar_t * txt, unsigned int size );

    explicit HpiInfo( const wchar_t * _name, std::wstring& _value );


    explicit HpiInfo( const wchar_t * _name, SaHpiUint8T ui8, UI8_Fmt fmt = UI8_Dec );

    explicit HpiInfo( const wchar_t * _name, SaHpiUint16T ui16, UI16_Fmt fmt = UI16_Dec );

    explicit HpiInfo( const wchar_t * _name, SaHpiInt32T i32, I32_Fmt fmt );

    explicit HpiInfo( const wchar_t * _name, SaHpiUint32T ui32, UI32_Fmt fmt = UI32_Dec );

    explicit HpiInfo( const wchar_t * _name, const SaHpiInt64T& i64, I64_Fmt fmt = I64_Dec );

    explicit HpiInfo( const wchar_t * _name, SaHpiFloat64T f64, F64_Fmt fmt = F64_FixedPoint );

    explicit HpiInfo( const wchar_t * _name, const SaHpiUint8T * binary, SaHpiUint16T len );

    template<class X>
    explicit HpiInfo( const wchar_t * _name, const X& x )
        : name( _name )
    {
        ToTxt( x, value );
    }


    // data
    std::wstring name;
    std::wstring value;
};

#endif // __HPI_INFO_H__

