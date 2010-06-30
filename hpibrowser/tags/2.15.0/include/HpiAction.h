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


#ifndef __HPI_ACTION_H__
#define __HPI_ACTION_H__

#include <string>


/************************************************
 * class HpiAction
 ***********************************************/
struct HpiAction
{
    explicit HpiAction( unsigned int _id, const std::wstring& _description )
        : id( _id ), description( _description )
    {
        // empty
    }


    // data
    int          id;
    std::wstring description;
};

/************************************************
 * class HpiActionShort
 ***********************************************/
struct HpiActionShort
{
    explicit HpiActionShort()
        : id( 0 )
    {
        // empty
    }

    explicit HpiActionShort( unsigned int _id )
        : id( _id )
    {
        // empty
    }

    explicit HpiActionShort( const HpiAction& action )
        : id( action.id )
    {
        // empty
    }


    // data
    int id;
};

#endif // __HPI_ACTION_H__

