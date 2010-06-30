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


#include <utility>

#include <QString>

#include "IconCache.h"


/************************************************
 * class cIconCache
 ***********************************************/
cIconCache * cIconCache::Instance()
{
    // TODO DTOR
    static cIconCache * instance = new cIconCache( ":/icons" );

    return instance;
}

cIconCache::cIconCache( const std::string& icon_dir_path )
    : m_icon_dir_path( icon_dir_path )
{
    // empty
    QString path = QString::fromStdString( m_icon_dir_path + "/" + "UNKNOWN" );
    m_cache["UNKNOWN"] = QIcon( path );
}

cIconCache::~cIconCache()
{
    // empty
}

const QIcon& cIconCache::GetIcon( const std::string& id )
{
    IconCacheType::const_iterator iter = m_cache.find( id );
    if ( iter != m_cache.end() ) {
        return iter->second;
    }

    QString path = QString::fromStdString( m_icon_dir_path + "/" + id );
    m_cache[id] = QIcon( path );

    return m_cache[id];
}
