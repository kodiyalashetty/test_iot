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


#ifndef __ICON_CACHE_H__
#define __ICON_CACHE_H__

#include <string>
#include <tr1/unordered_map>

#include <QIcon>


/************************************************
 * class cIconCache
 ***********************************************/
class cIconCache
{
public:

    static cIconCache * Instance();

    const QIcon& GetIcon( const std::string& id );

private:

    explicit cIconCache( const std::string& icon_dir_path );

    ~cIconCache();


    // data
    std::string m_icon_dir_path;

    typedef std::tr1::unordered_map<std::string, QIcon> IconCacheType;
    IconCacheType m_cache;
};


#endif // __ICON_CACHE_H__
