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


#include <QIcon>
#include <QSize>
#include <QString>

#include "EntriesWidget.h"
#include "IconCache.h"


/************************************************
 * class cEntriesWidget
 ***********************************************/
cEntriesWidget::cEntriesWidget( cHpiProvider& provider )
    : m_provider( provider )
{
    setObjectName( "HpiEntriesWidget" );

//    setViewMode( QListView::IconMode );
    setMovement( QListView::Static );
//    setIconSize( QSize( 32, 32 ) );
    setUniformItemSizes( true );

    connect( this,
             SIGNAL( itemActivated( QListWidgetItem * ) ),
             this,
             SLOT( activated( QListWidgetItem *)  ) );
}

void cEntriesWidget::Update()
{
    m_short_entries.clear();
    clear();

    std::deque<HpiEntry> entries;
    m_provider.GetEntries( entries );

    for ( unsigned int i = 0, n = entries.size(); i < n; ++i ) {
        QListWidgetItem * item;
        item = new QListWidgetItem( cIconCache::Instance()->GetIcon( "ENTRY" ),
                                    QString::fromStdWString( entries[i].description ),
                                    this );
        m_short_entries[ row( item ) ] = HpiEntryShort( entries[i] );
    }
}

void cEntriesWidget::activated( QListWidgetItem * item )
{
    QModelIndex index = indexFromItem( item );
    ShortEntries::const_iterator iter = m_short_entries.find( index.row() );
    if ( iter != m_short_entries.end() ) {
        m_provider.Enter( iter->second );
    } else {
        // TODO
    }
}

